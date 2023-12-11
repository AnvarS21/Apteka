from rest_framework import serializers
from django.contrib.auth import get_user_model

from review.models import Review

User = get_user_model()
class ReviewCreateSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source=User.id)
    username = serializers.ReadOnlyField(source=User.username)
    class Meta:
        model = Review
        exclude = 'created_at',

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source=User.id)
    username = serializers.ReadOnlyField(source=User.username)
    class Meta:
        model = Review
        fields = '__all__'