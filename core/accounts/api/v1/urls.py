from django.urls import path, include
from .views import RegistrationApiView, CustomTokenObtainPairView
#from rest_framework.authtoken.views import obtain_auth_token
from .views import CustomObtainAuthToken, CustomDiskardAuthToken, ChangePasswordAPIView, ProfileAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)


app_name = 'api_v1'

urlpatterns = [
    # registration
    path('registration/', RegistrationApiView.as_view(), name='registration'),

    # change password
    path('change_password/', ChangePasswordAPIView.as_view(), name='change_password'),

    # token
    path('token/login/', CustomObtainAuthToken.as_view(), name='token-login'),
    path('token/logout/', CustomDiskardAuthToken.as_view(), name='token-logout'),

    # profile
    path('profile/', ProfileAPIView.as_view(), name='profile' ),

    # jwt
    path('jwt/create/', CustomTokenObtainPairView.as_view(), name='jwt-create'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='jwt_refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(), name='jwt_verify'),
]
