from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(
        'Электронная почта',
              unique=True,
    )
    phone_number = PhoneNumberField(
        'Номер телефона',
        help_text='Пример: +996700777777'
    )

    REQUIRED_FIELDS = ['email', 'phone_number']

    def __str__(self):
        return f'{self.username}: {self.phone_number}'

    class Meta:
        verbose_name = 'Аккаунт'
        verbose_name_plural = 'Аккаунты'