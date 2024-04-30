from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Message, Notification


@receiver(post_save, sender=Message)
def message_sent(sender, instance, created, **kwargs):
    if created:
        # Создание уведомления для получателя сообщения
        Notification.objects.create(user=instance.user,
                                    message=f'Новое сообщение от {instance.sender.username}: {instance.text[:50]}...',
                                    category='message')

