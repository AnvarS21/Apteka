from django.shortcuts import render
from rest_framework.viewsets import mixins, GenericViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import ReviewSerializer, ReviewCreateSerializer
from .models import Review
from account.permissions import IsOwner, ReviewPermission


# Create your views here.

class ReviewViewSet(mixins.CreateModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   GenericViewSet):
    queryset = Review.objects.all()


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'create':
            return ReviewCreateSerializer
        return ReviewSerializer


    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated(), IsOwner()]
        elif self.action in ['destroy', 'update', 'partial_update']:
            return [ReviewPermission()]
        return [AllowAny()]