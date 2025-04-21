from django.db import models
from django.contrib.auth.models import User


class PageVisit(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    page_url = models.URLField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} посетил {self.page_url} в {self.timestamp}'


class UserAction(models.Model):
    ACTION_CHOICE = [
        ('registration', 'Registration'),
        ('event_participation', 'Event Participation'),
        ('content_interaction', 'Content Interaction')
        # Добавить необходимые действия по мере необходимости
    ]

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    action_type = models.CharField(max_length=50, choices=ACTION_CHOICE)
    timestamp = models.DateTimeField(auto_now_add=True)
    additional_info = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.user} perfomed {self.action_type} at {self.timestamp}'
