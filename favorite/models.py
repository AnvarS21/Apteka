from django.db import models
from django.contrib.auth import get_user_model

from product.models import Product

# Create your models here.
User = get_user_model()


class Favorite(models.Model):
    user = models.ForeignKey(User, related_name='favorites',
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='favorites',
                             on_delete=models.CASCADE)

    class Meta:
        unique_together = ['user', 'product']
