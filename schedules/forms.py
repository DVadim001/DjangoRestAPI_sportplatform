from django import forms
from .models import Schedule

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['title', 'description', 'start_time', 'end_time', 'location', 'is_private']
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
