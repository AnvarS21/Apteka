from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from rest_framework.routers import DefaultRouter

from product.views import ProductViewSet, CategoryViewSet

schema_view = get_schema_view(
   openapi.Info(
      title="BUYSELL's API",
      default_version='v1',
      description="Продай, Купи",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

swagger_urlpatterns = [
   path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

api_auth_urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api-auth/', include('rest_framework.urls')),
]

router = DefaultRouter()

router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)


api_urlpatterns = [
    path('schema/', include(swagger_urlpatterns)),
    path('auth/', include(api_auth_urlpatterns)),
    path('account/', include('account.urls')),
    path('reviews/', include('review.urls')),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),

] + router.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(api_urlpatterns)),

]


urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)