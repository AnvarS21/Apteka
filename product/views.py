from rest_framework.viewsets import ModelViewSet
from account import permissions
from product.models import Product
from rest_framework import permissions
from . import serializers

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.ProductListSerializer
        elif self.action == 'retrieve':
            return serializers.ProductSerializer

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            return [permissions.AllowAny]
        return [permissions.IsAdmin]

