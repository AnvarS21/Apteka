import random
import string

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.dispatch import receiver

from django_rest_passwordreset.signals import reset_password_token_created


User = get_user_model()


def generate_token():
    symbols = string.ascii_letters + string.digits
    token = ''.join(random.choice(symbols) for _ in range(20))
    return token


@receiver(post_save, sender=User)
def send_confirm_user(sender, instance, created, **kwargs):
    if created:
        token = generate_token()
        instance.token = token
        instance.save()
        subject = f'Подтверждение аккаунта.'
        message = f'''Приветствуем {instance.username}.
Введите ниже сгенерированный токен на сайте:
                {token}
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

