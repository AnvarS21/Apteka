from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet, ConfirmUserView
router = DefaultRouter()

router.register(r'users', CustomUserViewSet, basename='users')

urlpatterns = [
    path('confirm/', ConfirmUserView.as_view())
] + router.urls
