import datetime

from django.db import models
from django.db.models.fields import CharField
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator 


class Sport(models.Model):
    name = CharField(max_length=200)
    color = CharField(max_length=10, null=True, blank=True)
    coefficient = models.FloatField(null=True, blank=True)
    
    def __str__(self):
        return self.name


class HealthIssue(models.Model):
    runner = models.ForeignKey(
        User,
        default=1,
        on_delete=models.CASCADE,
    )
    name = CharField(max_length=200)
    traumatologic = models.BooleanField()
    
    def __str__(self):
        return self.name


class Label(models.Model):
    runner = models.ForeignKey(
        User,
        default=1,
        on_delete=models.CASCADE,
    )
    name = CharField(max_length=200)
    color = CharField(max_length=10, null=True, blank=True)
    
    def __str__(self):
        return self.name


class Session(models.Model):
    runner = models.ForeignKey(
        User,
        default=1,
        on_delete=models.CASCADE,
    )
    start_time = models.DateTimeField()
    name = models.CharField(max_length=200, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    difficulty = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    labels = models.ManyToManyField(Label, blank=True)
    
    def __str__(self):
        return str(self.start_time)[:10] + " | " + self.name


class Gear(models.Model):
    runner = models.ForeignKey(
        User,
        default=1,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


class Exercise(models.Model):
    runner = models.ForeignKey(
        User,
        default=1,
        on_delete=models.CASCADE,
    )
    sport = models.ForeignKey(
        Sport,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=200, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name



class Activity(models.Model):
    runner = models.ForeignKey(
        User,
        default=1,
        on_delete=models.CASCADE,
    )
    session = models.ForeignKey(
        Session,
        on_delete=models.CASCADE,
    )
    duration = models.DurationField()
    sport = models.ForeignKey(
        Sport,
        on_delete=models.CASCADE,
    )
    medium_intensity = models.DurationField(default=datetime.timedelta())
    high_intensity = models.DurationField(default=datetime.timedelta())
    intervals = CharField(max_length=10, null=True, blank=True)
    gears = models.ManyToManyField(Gear, blank=True)
    exercises = models.ManyToManyField(Exercise, blank=True)

    def __str__(self):
        return self.session.name + " " + self.sport.name


class SessionHealthMonitoring(models.Model):
    runner = models.ForeignKey(
        User,
        default=1,
        on_delete=models.CASCADE,
    )
    session = models.ForeignKey(
        Session,
        on_delete=models.CASCADE,
    )
    pain = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    health_issue = models.ForeignKey(
        HealthIssue,
        on_delete=models.CASCADE,
    )
    incident = models.BooleanField(default=False)
    
    def __str__(self):
        return self.session.name + " " + self.health_issue.name


class DailyMonitoring(models.Model):
    runner = models.ForeignKey(
        User,
        default=1,
        on_delete=models.CASCADE,
    )
    date = models.DateField(default=datetime.date.today)
    feeling = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])

    def __str__(self):
        return str(self.date)


class DailyHealthMonitoring(models.Model):
    runner = models.ForeignKey(
        User,
        default=1,
        on_delete=models.CASCADE,
    )
    daily_monitoring = models.ForeignKey(
        DailyMonitoring,
        on_delete=models.CASCADE,
    )
    pain = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    health_issue = models.ForeignKey(
        HealthIssue,
        on_delete=models.CASCADE,
    )
    
    def __str__(self):
        return str(self.daily_monitoring.date) + " " + self.health_issue.name