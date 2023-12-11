from django.contrib.auth import get_user_model
from rest_framework.response import Response

from rest_framework import viewsets, generics, permissions

from .permissions import IsOwner, IsAdmin

from .serializers import CustomUserSerializer, CustomUserCreateSerializer, ConfirmUserSerializer

User = get_user_model()


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return CustomUserCreateSerializer
        return CustomUserSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny(), ]
        elif self.action == 'list':
            return [IsAdmin(), ]
        return [IsOwner(), ]


class ConfirmUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = ConfirmUserSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        user = User.objects.filter(token=request.data['token'])
        if user:
            user[0].is_active = True
            user[0].save()
            return Response( 'OK', status=200)
        return Response('Not Found', status=404)






