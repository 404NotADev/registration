from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from users.views import RegisterView, ProfileView
from logs.signals import CustomTokenObtainPairView

# Swagger / Redoc (drf-spectacular)
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Users
    path('api/v1/users/register/', RegisterView.as_view(), name='register'),
    path('api/v1/users/me/', ProfileView.as_view(), name='profile'),
    
    # JWT
    path('api/v1/auth/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Logs
    path('api/v1/logs/', include('logs.urls')),

    # Schema and Docs
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/docs/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
