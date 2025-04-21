from django.contrib import admin
from .models import Message, Notification


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'recipient', 'subject', 'sent_at', 'read_at')
    list_filter = ('sent_at', 'read_at')
    search_fields = ('subject', 'body')


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'created_at', 'is_seen')
    list_filter = ('created_at', 'is_seen')
    search_fields = ('message',)
