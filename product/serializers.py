from rest_framework import serializers

from product.models import Product, Category


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



