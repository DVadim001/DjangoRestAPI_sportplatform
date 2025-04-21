from django.db import models
from django.contrib.auth.models import User
from events.models import Event


class Equipment(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    status_choices = [
        ('available', 'Available'),
        ('in_use', 'In Use'),
        ('maintenance', 'Maintenance'),
    ]
    status = models.CharField(max_length=50, choices=status_choices, default='available')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class EquipmentReservation(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} reserved {self.equipment} for {self.event} from {self.start_date} to {self.end_date}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.equipment.status != 'in_use':
            self.equipment.status = 'in_use'
            self.equipment.save()
