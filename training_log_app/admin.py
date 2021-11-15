from django.contrib import admin
from django.db import models
from django.forms.widgets import Textarea, CheckboxSelectMultiple

from .widgets import RangeInput

from .models import (
    Sport,
    HealthIssue,
    Label,
    Session,
    Activity,
    SessionHealthMonitoring,
    DailyMonitoring,
    DailyHealthMonitoring,
    Gear,
    Exercise
)


class ActivityInline(admin.StackedInline):
    model = Activity
    extra = 1
    fields = ('session', 'duration', 'sport', ('medium_intensity', 'high_intensity'), 'intervals', ('gears', 'exercises'))
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple()}
    }


class SessionHealthMonitoringInline(admin.StackedInline):
    model = SessionHealthMonitoring
    extra = 0
    exclude = ['runner']
    formfield_overrides = {
        models.IntegerField: {'widget': RangeInput(attrs={"min": 0, "max": 10}) }
    }


class DailyHealthMonitoringInline(admin.StackedInline):
    model = DailyHealthMonitoring
    extra = 0
    exclude = ['runner']
    formfield_overrides = {
        models.IntegerField: {'widget': RangeInput(attrs={"min": 0, "max": 10}) }
    }


class HealthIssueAdmin(admin.ModelAdmin):
    exclude = ['runner']


class LabelAdmin(admin.ModelAdmin):
    exclude = ['runner']


class SessionAdmin(admin.ModelAdmin):
    inlines = [
        ActivityInline,
        SessionHealthMonitoringInline
    ]
    exclude = ['runner']
    ordering = ('-start_time',)
    formfield_overrides = {
        models.IntegerField: {'widget': RangeInput(attrs={"min": 0, "max": 10}) },
        models.TextField: {'widget': Textarea(attrs={"rows": 3}) },
        models.ManyToManyField: {'widget': CheckboxSelectMultiple()}
    }


class ActivityAdmin(admin.ModelAdmin):
    exclude = ['runner']


class SessionHealthMonitoringAdmin(admin.ModelAdmin):
    exclude = ['runner']
    formfield_overrides = {
        models.IntegerField: {'widget': RangeInput(attrs={"min": 0, "max": 10}) }
    }


class DailyMonitoringAdmin(admin.ModelAdmin):
    inlines = [DailyHealthMonitoringInline]
    exclude = ['runner']
    ordering = ('-date',)
    formfield_overrides = {
        models.IntegerField: {'widget': RangeInput(attrs={"min": 0, "max": 10}) }
    }


class DailyHealthMonitoringAdmin(admin.ModelAdmin):
    exclude = ['runner']
    formfield_overrides = {
        models.IntegerField: {'widget': RangeInput(attrs={"min": 0, "max": 10}) }
    }


class GearAdmin(admin.ModelAdmin):
    exclude = ['runner']


class ExerciseAdmin(admin.ModelAdmin):
    exclude = ['runner']


admin.site.register(Sport)
admin.site.register(HealthIssue, HealthIssueAdmin)
admin.site.register(Label, LabelAdmin)
admin.site.register(Session, SessionAdmin)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(SessionHealthMonitoring, SessionHealthMonitoringAdmin)
admin.site.register(DailyMonitoring, DailyMonitoringAdmin)
admin.site.register(DailyHealthMonitoring, DailyHealthMonitoringAdmin)
admin.site.register(Gear, GearAdmin)
admin.site.register(Exercise, ExerciseAdmin)