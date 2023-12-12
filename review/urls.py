from rest_framework.routers import DefaultRouter
from django.urls import path, include
from review.views import ReviewViewSet


router = DefaultRouter()
router.register('', ReviewViewSet)



urlpatterns = [

] + router.urls