from django.contrib.auth import get_user_model
from rest_framework import serializers
User = get_user_model()


class CustomUserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'phone_number',
            'first_name',
            'last_name',
            'password',
        )

    def create(self, validate_data):
        if validate_data['first_name'] and validate_data['last_name']:
            user = User.objects.create(
                username=validate_data['username'],
                email=validate_data['email'],
                phone_number=validate_data['phone_number'],
                first_name=validate_data['first_name'],
                last_name=validate_data['last_name'],
                password=validate_data['password'],
            )
            return user
        else:
            user = User.objects.create(
                username=validate_data['username'],
                email=validate_data['email'],
                phone_number=validate_data['phone_number'],
                password=validate_data['password'],
            )
            return user



class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'phone_number',
            'first_name',
            'last_name',
        )