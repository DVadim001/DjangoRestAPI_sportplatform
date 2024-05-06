from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    location = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)


class Result(models.Model):
    event = models.ForeignKey(Event, related_name="results", on_delete=models.CASCADE)
    participant = models.ForeignKey(User, related_name="results", on_delete=models.CASCADE)
    score = models.FloatField()
    position = models.IntegerField()

    class Meta:
        ordering = ['position']
