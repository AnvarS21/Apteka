from django.db import models

# Create your models here.

# class Category(models.Model):
#     category = models.CharField(max_length=100,
#                                 verbose_name='Категория')
#
#     def __str__(self):
#         return self.category
#
#     class Meta:
#         verbose_name = 'Категория'
#         verbose_name_plural = 'Категории'

class Group(models.Model):
    group = models.CharField(max_length=100,
                             verbose_name='Лекарственная группа')

    def __str__(self):
        return self.group

    class Meta:
        verbose_name = 'Лекарственная группа'
        verbose_name_plural = 'Лекарственные группы'

class Product(models.Model):
    drug_group = models.ForeignKey(Group, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=150,
                             verbose_name='Название')
    desc = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='images/',
                              null=True,
                              blank=True,
                              verbose_name='Изображение')
    price = models.PositiveIntegerField(verbose_name='Цена')
    quantity = models.PositiveIntegerField(verbose_name='Количество')

    def __str__(self):
        return f'{self.title}, {self.desc[:25]}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

