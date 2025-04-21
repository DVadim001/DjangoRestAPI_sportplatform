from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from .models import Schedule
from communication.models import Notification


@receiver(post_save, sender=Schedule)
def schedule_created_or_updated(sender, instance, created, **kwargs):
    # Определить, было ли событие только что создано или обновлено
    if created:
        message = f'Новое событие в вашем календаре: {instance.title}'
    else:
        message = f'Обновлено событие в вашем календаре: {instance.title}'

    # Отправляемуведовление пользователю
    Notification.objects.create(
        user=instance.user,
        message=message,
        category='schedule'
    )
