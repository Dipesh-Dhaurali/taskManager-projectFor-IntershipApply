from django.urls import path
from .views import landing_page, login_page, register_page, RegisterAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # Template URLs
    path('', landing_page, name='landing'),
    path('login/', login_page, name='login_page'),
    path('register/', register_page, name='register_page'),

    # API URLs
    path('api/register/', RegisterAPIView.as_view(), name='api_register'),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
