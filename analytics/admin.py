from django.contrib import admin
from .models import PageVisit, UserAction


@admin.register(PageVisit)
class PageVisitAdmin(admin.ModelAdmin):
    list_display = ('user', 'path', 'method', 'timestamp')
    search_fields = ('user__username', 'path')
    list_filter = ('method', 'timestamp')


@admin.register(UserAction)
class UserActionAdmin(admin.ModelAdmin):
    list_display = ('user', 'action_type', 'timestamp')
    search_fields = ('user__username', 'action_type')
    list_filter = ('action_type', 'timestamp')
