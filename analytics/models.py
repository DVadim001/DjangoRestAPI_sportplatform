from django.db import models
from django.contrib.auth.models import User


class PageVisit(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    path = models.CharField(max_length=255)
    method = models.CharField(max_length=10)
    user_agent = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} — {self.path} [{self.timestamp.strftime("%Y-%m-%d %H:%M:%S")}]'


class UserAction(models.Model):
    ACTION_CHOICE = [
        ('registration', 'Registration'),
        ('event_signup', 'Event Signup'),
        ('event_create', 'Event Create'),
        ('content_interaction', 'Content Interaction'),
    ]

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    action_type = models.CharField(max_length=50, choices=ACTION_CHOICE)
    timestamp = models.DateTimeField(auto_now_add=True)
    additional_info = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.user} — {self.get_action_type_display()} @ {self.timestamp.strftime("%Y-%m-%d %H:%M:%S")}'
