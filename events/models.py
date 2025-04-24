from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    description = models.TextField(blank=True)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Participant(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='participants')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20,
        choices=[
            ('registered', 'Registered'),
            ('waiting', 'Waiting'),
            ('cancelled', 'Cancelled')
        ]
    )

    def __str__(self):
        return f'{self.user.username} - {self.event.name}'


class EventImage(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='event_images/')

    def __str__(self):
        return f'Image for {self.event.name}'


class Notification(models.Model):
    notification_type = models.CharField(max_length=50)
    to_user = models.ForeignKey(User, related_name='notifications', on_delete=models.CASCADE)
    from_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, related_name='notifications', on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    text_preview = models.CharField(max_length=90, blank=True)
    is_seen = models.BooleanField(default=False)

    def __str__(self):
        return f'Уведомление для {self.to_user.username} - {self.notification_type}'
