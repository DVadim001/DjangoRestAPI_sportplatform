from django import forms
from .models import Message, Notification


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['recipient', 'subject', 'body']


class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ['message', 'is_seen']
