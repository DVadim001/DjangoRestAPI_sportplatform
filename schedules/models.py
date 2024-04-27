from django.db import models
from django.conf import settings


class Schedule(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='schedule')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    is_private = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.start_time} - {self.end_time}: {self.title} ({self.user.username})'


# Дополнительная модель, если нужна категорияпланирования
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
