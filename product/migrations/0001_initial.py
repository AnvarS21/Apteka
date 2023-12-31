# Generated by Django 5.0 on 2023-12-11 18:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('desc', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='image', verbose_name='Изображение')),
                ('price', models.PositiveIntegerField(verbose_name='Цена')),
                ('quantity', models.PositiveSmallIntegerField(verbose_name='Количесвто')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='product.category', verbose_name='Лекарственная группа')),
            ],
        ),
    ]
