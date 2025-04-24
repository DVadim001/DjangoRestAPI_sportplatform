from django.db import models
from django.contrib.auth.models import User


class PageVisit(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    page_url = models.URLField()
    path = models.CharField(max_length=500)
    method = models.CharField(max_length=10)
    user_agent = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} посетил {self.page_url} в {self.timestamp}'


class UserAction(models.Model):
    ACTION_CHOICE = [
        ('registration', 'Registration'),
        ('event_participation', 'Event Participation'),
        ('content_interaction', 'Content Interaction'),
    ]

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    action_type = models.CharField(max_length=50, choices=ACTION_CHOICE)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    additional_info = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.user} performed {self.action_type} at {self.timestamp}'
