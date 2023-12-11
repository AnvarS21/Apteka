from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=100,
                             verbose_name='Название')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Product(models.Model):
    title = models.CharField(max_length=100,
                             verbose_name='Название',)
    desc = models.TextField(verbose_name='Описание',)
    image = models.ImageField(upload_to='image',
                              verbose_name='Изображение',
                              )
    price = models.PositiveIntegerField(verbose_name='Цена',)
    group = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE,
                              verbose_name='Лекарственная группа')
    quantity = models.PositiveSmallIntegerField(verbose_name='Количесвто')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Лекарство'
        verbose_name_plural = 'Лекарства'