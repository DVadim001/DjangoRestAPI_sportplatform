from django.db import models
from django.contrib.auth.models import User

class ServiceType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(ServiceType, on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10, default='UZS')
    status = models.CharField(max_length=20, choices=[('pending', 'Ожидается'), ('paid', 'Оплачено'), ('failed', 'Ошибка')], default='pending')
    transaction_id = models.CharField(max_length=255, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} — {self.amount} {self.currency} ({self.get_status_display()})"
