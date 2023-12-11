from rest_framework.viewsets import ModelViewSet
from account.permissions import IsAdmin
from product.models import Product
from rest_framework import permissions
from . import serializers

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    # permission_classes = [IsAdmin()]

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.ProductListSerializer
        elif self.action in ('create', 'update', 'partial_update'):
            return serializers.ProductSerializer
        return serializers.ProductDetailSerializer

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            return [permissions.AllowAny(), ]
        return [IsAdmin(), ]

    @action
