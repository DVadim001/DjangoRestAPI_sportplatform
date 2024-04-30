from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Event, Participant, Notification


@receiver(post_save, sender=Event)
def event_created(sender, instance, created, **kwargs):
    if created:
        # Отправляем увеломление всем пользователям о новом событии
        users = User.objects.all()
        for user in users:
            Notification.objects.create(
                notification_type='new_event',
                to_user=user,
                from_user=instance.organizer,
                event=instance,
                text_preview=f'Новое событие: {instance.name}'
            )
