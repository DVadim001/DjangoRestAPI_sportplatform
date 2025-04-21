from django.db import models
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User


def default_privacy_settings():
    return {}


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField('О себе', blank=True)  # О себе

    # Контактные данные
    phone_number = PhoneNumberField()
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, default='')

    # Профиль атлета
    birth_date = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')], blank=True, default='')
    height = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    experience_level = models.CharField(max_length=50, blank=True, default='')  # Уровень подготовки
    preferred_sports = models.TextField(blank=True, default='')  # Предпочтения
    participation_history = models.TextField(blank=True, default='')  # История участия
    coaching_details = models.TextField(blank=True, default='')  # Тренерская информация
    medical_information = models.TextField(blank=True, default='')  # Медицинская информация
    equipment = models.TextField(blank=True, default='')  # Оборудование и инвентарь
    club_memberships = models.ManyToManyField('clubs.Club', related_name='user_profile', blank=True)  # Членство в клубах и командах
    subscriptions = models.ManyToManyField(User, related_name='followers', blank=True)  # Подписки и членство

    # Настройка конфеденциальности
    privacy_settings = models.JSONField(blank=True, default=default_privacy_settings)
    receive_newsletters = models.BooleanField(default=True)
    public_profile = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}'s profile"
