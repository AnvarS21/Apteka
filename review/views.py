from django.shortcuts import render
from rest_framework.viewsets import mixins, GenericViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from . import serializers
from review.models import Review
from account.permissions import IsAdmin, IsOwner


# Create your views here.

class ReviewViewSet(mixins.CreateModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   GenericViewSet):
    queryset = Review.objects.all()


    def get_serializer_class(self):
        if self.action == 'create':
            return serializers.ReviewCreateSerializer
        return serializers.ReviewSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated(), ]
        if self.action in ('destroy', 'update', 'partial_update'):
            return [IsOwner(), ]
        return [AllowAny(), ]