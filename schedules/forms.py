from django import forms
from .models import Schedule


class ScheduleForm(forms.ModelForm):
    model = Schedule
    fields = ['title', 'description', 'start_time', 'end_time']
    widgets = {
        'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
    }
