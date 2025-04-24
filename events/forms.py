from django import forms
from .models import Event, Participant
from django.forms.widgets import DateTimeInput


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'start_time', 'end_time', 'location']
        widgets = {
            'start_time': DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': 'form-control',
                'placeholder': 'Начало события'
            }),
            'end_time': DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': 'form-control',
                'placeholder': 'Окончание события'
            }),
        }
        labels = {
            'name': 'Название',
            'description': 'Описание',
            'start_time': 'Дата и время начала',
            'end_time': 'Дата и время окончания',
            'location': 'Место проведения',
        }


class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['user']
