from rest_framework.filters import SearchFilter
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from account.permissions import IsAdmin
from product.models import Product, Category
from review.serializers import ReviewSerializer
from .filters import ProductFilter, CategoryFilter

from .serializers import CategorySerializer
from .serializers import ProductSerializer, ProductListSerializer, ProductDetailSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['title', 'desc']
    filterset_class = ProductFilter

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
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['title', 'products']
    filterset_class = CategoryFilter


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