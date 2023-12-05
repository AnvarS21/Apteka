from django.contrib.auth import get_user_model

from rest_framework import viewsets, permissions

from .serializers import CustomUserSerializer, CustomUserCreateSerializer

User = get_user_model()

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]

    def get_serializer_class(self):
        if self.action == 'create':
            return CustomUserCreateSerializer
        return CustomUserSerializer