from django import forms
from .models import Event, Participant


class EventForm(forms.ModelForm):
    model = Event
    fields = ['name',
              'start_date',
              'end_date',
              'category',
              'locations',
              'description',
              'organizer'
              ]

    widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control'}),
        'start_date': forms.DateInput(format='%Y-%m-%d', attrs={'class': 'form-control', 'type': 'date'}),
        'end_date': forms.DateInput(format='%Y-%m-%d', attrs={'class': 'form-control', 'type': 'date'}),
        'category': forms.Select(attrs={'class': 'form-control'}),
        'locations': forms.TextInput(attrs={'class': 'form-control'}),
        'description': forms.Textarea(attrs={'class': 'form-control'}),
        'organizer': forms.TextInput(attrs={'class': 'form-control'})
    }


class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['status']
