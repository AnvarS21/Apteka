from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from account.permissions import IsAdmin
from product.models import Product, Category
from review.serializers import ReviewSerializer

from .serializers import CategorySerializer
from .serializers import ProductSerializer, ProductListSerializer, ProductDetailSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    # permission_classes = [IsAdmin()]

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        elif self.action in ('create', 'update', 'partial_update'):
            return ProductSerializer
        return ProductDetailSerializer

    def get_permissions(self):
        if self.action in ('list', 'retrieve', 'reviews'):
            return [permissions.AllowAny(), ]
        return [IsAdmin(), ]

    @action(['GET'], detail=True)
    def reviews(self, request, pk):
        product = self.get_object()
        reviews = product.reviews.all()
        serializer = ReviewSerializer(instance=reviews, many=True)
        return Response(serializer.data, status=200)





class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()

    def get_serializer_class(self):
        return CategorySerializer


    def get_permissions(self):
        if self.action in ('list', 'products', 'retrieve'):
            return [permissions.AllowAny(), ]
        return [IsAdmin(), ]

    @action(['GET'], detail=True)
    def products(self, request, pk):
        category = self.get_object()
        products = category.products.all()
        serializer = ProductListSerializer(instance=products, many=True)
        return Response(serializer.data, status=200)