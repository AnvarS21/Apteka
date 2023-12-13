from rest_framework import serializers
from django.contrib.auth import get_user_model

from favorite.serializers import FavoriteSerializer
from product.models import Product, Category

User = get_user_model()

class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'image', 'price')


class ProductDetailSerializer(serializers.ModelSerializer):
    status = 'В наличии' if Product.quantity != 0 else 'Нет в наличии'
    class Meta:
        model = Product
        exclude = 'quantity',

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class UserAddFavorites(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = 'id',

class UserFavoritesSerializer(serializers.ModelSerializer):
    favorites = FavoriteSerializer(many=True)
    class Meta:
        model = User
        fields = 'favorites',



