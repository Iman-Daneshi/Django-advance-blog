from django.urls import path
#from rest_framework.authtoken.views import obtain_auth_token
from ..views import ProfileAPIView


urlpatterns = [
    # profile
    path('', ProfileAPIView.as_view(), name='profile'),
]