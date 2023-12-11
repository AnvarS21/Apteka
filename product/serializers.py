from rest_framework import serializers

from product.models import Product


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'image', 'price')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = 'quantity'