from django.db import models
from django.conf import settings


class Message(models.Model):
    sender = models. ForeignKey(settings.AUTH_USER_MODEL, related_name='sent_message', on_delete=models.CASCADE)
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='received_messages', on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    body = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    read_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'From {self.sender} to {self.recipient} - {self.subject}'


class Notification(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='communication_notifications', on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_seen = models.BooleanField(default=False)

    def __str__(self):
        return f'Notification for {self.user}: {self.message}'
