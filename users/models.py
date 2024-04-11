from django.db import models
from django.conf import settings


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # Контактные данные
    phone_number = models.CharField(max_length=15, blank=True, default='')
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, default='')

    # Профиль атлета
    birth_date = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')], blank=True, default='')
    height = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    # Уровень подготовки
    experience_level = models.CharField(max_length=50, blank=True, default='')

    # Предпочтения
    preferred_sports = models.TextField(blank=True, default='')

    # История участия
    participation_history = models.TextField(blank=True, default='')

    # Тренерская информация
    coaching_details = models.TextField(blank=True, default='')

    # Медицинская информация
    medical_information = models.TextField(blank=True, default='')

    # Оборудование и инвентарь
    equipment = models.TextField(blank=True, default='')

    # Членство в клубах и командах
    club_memberships = models.TextField(blank=True, default='')

    # Подписки и членство
    subscriptions = models.TextField(blank=True, default='')

    # Настройка конфеденциальности
    privacy_settings = models.JSONField(blank=True, default=dict)

    def __str__(self):
        return self.user.username
