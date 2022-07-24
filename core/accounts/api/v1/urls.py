from django.urls import path, include
from .views import RegistrationApiView
from rest_framework.authtoken.views import obtain_auth_token


app_name = 'api_v1'

urlpatterns = [
    path('registration/', RegistrationApiView.as_view(), name='registration'),
    path('api-token-auth/', obtain_auth_token)
]
