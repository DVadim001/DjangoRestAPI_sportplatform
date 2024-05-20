from django import forms
from .models import Equipment, EquipmentReservation

class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['name', 'description', 'status']

class EquipmentReservationForm(forms.ModelForm):
    class Meta:
        model = EquipmentReservation
        fields = ['start_date', 'end_date', 'event']
