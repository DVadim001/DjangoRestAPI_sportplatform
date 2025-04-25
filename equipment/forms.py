from django import forms
from .models import Equipment, EquipmentReservation
from django.core.exceptions import ValidationError

class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['name', 'description', 'quantity']
        labels = {
            'name': 'Название',
            'description': 'Описание',
            'quantity': 'Количество',
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

class EquipmentReservationForm(forms.ModelForm):
    class Meta:
        model = EquipmentReservation
        fields = ['start_date', 'end_date', 'event']

    def __init__(self, *args, **kwargs):
        self.equipment = kwargs.pop('equipment', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        start = cleaned_data.get('start_date')
        end = cleaned_data.get('end_date')

        if self.equipment and start and end:
            overlaps = EquipmentReservation.objects.filter(
                equipment=self.equipment,
                start_date__lt=end,
                end_date__gt=start,
            )
            if self.instance.pk:
                overlaps = overlaps.exclude(pk=self.instance.pk)

            if overlaps.exists():
                raise ValidationError('Это оборудование уже забронировано на выбранные даты.')

        return cleaned_data
