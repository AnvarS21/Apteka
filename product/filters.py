from django.db.models import Q
from django_filters import rest_framework as django_filters

from .models import Product, Category


class ProductFilter(django_filters.FilterSet):
    field_name = django_filters.Filter(lookup_expr='exact')
    price__gte = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    price__lte = django_filters.NumberFilter(field_name='price', lookup_expr='lte')


    class Meta:
        model = Product
        fields = ['title', 'desc']


class CategoryFilter(django_filters.FilterSet):
    field_name = django_filters.Filter(lookup_expr='exact')
    class Meta:
        model = Category
        fields = ['title', 'products']