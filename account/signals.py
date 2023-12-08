from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.urls import reverse

from django_rest_passwordreset.signals import reset_password_token_created


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

@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    subject = f'Восстаровление пароля.'
    message = f'''Приветствуем {reset_password_token.user.username}.
Вставьте ниже сгенерированный токен: 
            {reset_password_token.key}
    '''
    from_email = settings.EMAIL_HOST_USER
    to_email = reset_password_token.user.email
    send_mail(subject, message, from_email, [to_email])