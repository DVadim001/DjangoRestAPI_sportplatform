from django.contrib import admin
from .models import Schedule, Category


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['title', 'start_time', 'end_time', 'user', 'is_private']


admin.site.register(Category)
