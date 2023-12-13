from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet, ConfirmUserView, UserFavoriteViewSet

router = DefaultRouter()

router.register(r'users', CustomUserViewSet, basename='users')
router.register(r'favorites', UserFavoriteViewSet)

urlpatterns = [
    path('confirm/', ConfirmUserView.as_view()),
] + router.urls
