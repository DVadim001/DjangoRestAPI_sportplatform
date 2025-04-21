from django.contrib import admin
from .models import PageVisit, UserAction


@admin.register(PageVisit)
class PageVisitAdmin(admin.ModelAdmin):
    list_display = ('user', 'page_url', 'timestamp')
    search_fields = ('user__username', 'page_url')
    list_filter = ('timestamp',)


@admin.register(UserAction)
class UserActionAdmin(admin.ModelAdmin):
    list_display = ('user', 'action_type', 'timestamp', 'additional_info')
    search_fields = ('user__username', 'action_type')
    list_filter = ('action_type', 'timestamp')
