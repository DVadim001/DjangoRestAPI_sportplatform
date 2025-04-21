from django import forms
from .models import Club


class ClubForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = ['name', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'cols': 40, 'rows': 5}),
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }
