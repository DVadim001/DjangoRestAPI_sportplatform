from django.db import models
from django.contrib.auth.models import User


class Club(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    members = models.ManyToManyField(User, through='Membership')
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_clubs', null=True, blank=True, default=None)

    def __str__(self):
        return self.name


class Membership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} состоит в клубах {self.club.name}'
