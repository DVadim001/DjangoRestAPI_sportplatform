from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    description = models.TextField(blank=True)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    tags = models.ManyToManyField(Tag, related_name='events')

    def __str__(self):
        return self.name


class Participant(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='participants')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[('registered', 'Registered'),
                                                      ('waiting', 'Waiting'),
                                                      ('cancelled', 'Cancelled')])

    def __str__(self):
        return f'{self.user.username} - {self.event.name}'


class EventImage(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='event_images/')

    def __str__(self):
        return f'Image for {self.event.name}'


class EventTag(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.tag.name} associated with {self.event.name}'
