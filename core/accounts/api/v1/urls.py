from django.urls import path, include
from .views import RegistrationApiView
#from rest_framework.authtoken.views import obtain_auth_token
from .views import CustomObtainAuthToken, CustomDiskardAuthToken
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)


app_name = 'api_v1'

urlpatterns = [
    path('registration/', RegistrationApiView.as_view(), name='registration'),
    path('token/login/', CustomObtainAuthToken.as_view(), name='token-login'),
    path('token/logout/', CustomDiskardAuthToken.as_view(), name='token-logout'),
    path('jwt/create/', TokenObtainPairView.as_view(), name='jwt-create'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='jwt_refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(), name='jwt_verify'),
]
