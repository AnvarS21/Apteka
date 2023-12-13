from django.db import models
from django.contrib.auth import get_user_model

from product.models import Product

# Create your models here.
User = get_user_model()


class Review(models.Model):
    RATING_CHOICES = (
        (1, 'Too bad!'), (2, 'Bad!'),
        (3, 'Normal!'), (4, 'Good!'),
        (5, 'Excellent!')
    )
    rating = models.PositiveSmallIntegerField(
        choices=RATING_CHOICES)
    user = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    body = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body


