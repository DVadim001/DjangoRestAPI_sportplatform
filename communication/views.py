from django.shortcuts import render

from rest_framework import viewsets
from .models import Message, Notification
from .serializers import MessageSerializer, NotificationSerializer


class MeageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.filter(is_seen=False)
    serializer_class = NotificationSerializer
