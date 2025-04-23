from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from clubs.models import Club

# 👉 Добавляем функцию, чтобы использовать её как default=...
def default_privacy_settings():
    return {
        "show_email": True,
        "show_birth_date": False,
        "show_phone": False,
        "allow_messages": True
    }

class UserProfile(models.Model):
    class GenderChoices(models.TextChoices):
        MALE = 'M', 'Мужской'
        FEMALE = 'F', 'Женский'
        OTHER = 'O', 'Другое'

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, verbose_name=_("Аватар"))
    bio = models.TextField(blank=True, verbose_name=_("О себе"))

    phone_number = PhoneNumberField(blank=True, null=True, verbose_name=_("Телефон"))
    birth_date = models.DateField(blank=True, null=True, verbose_name=_("Дата рождения"))
    gender = models.CharField(max_length=1, choices=GenderChoices.choices, blank=True, null=True, verbose_name=_("Пол"))
    height = models.FloatField(blank=True, null=True, verbose_name=_("Рост (см)"))
    weight = models.FloatField(blank=True, null=True, verbose_name=_("Вес (кг)"))
    experience_level = models.CharField(max_length=100, blank=True, verbose_name=_("Опыт"))
    preferred_sports = models.CharField(max_length=255, blank=True, verbose_name=_("Предпочтительные виды спорта"))
    medical_information = models.TextField(blank=True, verbose_name=_("Медицинская информация"))
    equipment = models.CharField(max_length=255, blank=True, verbose_name=_("Инвентарь"))

    club_memberships = models.ManyToManyField('clubs.Club', related_name='user_memberships', blank=True)
    subscriptions = models.ManyToManyField(User, blank=True, related_name='subscribers')

    receive_newsletters = models.BooleanField(default=False, verbose_name=_("Получать новости"))
    public_profile = models.BooleanField(default=True, verbose_name=_("Публичный профиль"))

    def __str__(self):
        return f"Профиль {self.user.username}"


class UserSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='settings')
    receive_newsletters = models.BooleanField(default=False, verbose_name="Получать новости")
    public_profile = models.BooleanField(default=True, verbose_name="Публичный профиль")

    # 👉 Добавляем поле, которое использует default_privacy_settings
    privacy_settings = models.JSONField(default=default_privacy_settings, blank=True, verbose_name="Настройки приватности")

    def __str__(self):
        return f"Настройки {self.user.username}"
