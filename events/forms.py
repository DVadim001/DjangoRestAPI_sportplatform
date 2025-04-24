from django import forms
from .models import Event, Participant
from taggit.forms import TagWidget
from django.forms.widgets import DateTimeInput

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'start_time', 'end_time', 'location', 'tags']
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
            'tags': TagWidget(attrs={
                'class': 'form-control',
                'placeholder': 'Введите теги'
            }),
        }
        labels = {
            'name': 'Название',
            'description': 'Описание',
            'start_time': 'Дата и время начала',
            'end_time': 'Дата и время окончания',
            'location': 'Место проведения',
            'tags': 'Теги',
        }

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['user']
