from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail

User = get_user_model()


@receiver(post_save, sender=User)
def send_notification_user(sender, instance, created, **kwargs):
    if created:
        subject = f'Уведомление о регистрации.'
        message = f'''Приветствуем {instance.username}.
Вы успешно зергистрированы!
'''
        from_email = settings.EMAIL_HOST_USER
        to_email = instance.email
        send_mail(subject, message, from_email, [to_email])

