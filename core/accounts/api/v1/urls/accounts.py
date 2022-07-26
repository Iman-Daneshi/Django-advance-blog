from django.urls import path, include
from ..views import (RegistrationApiView, CustomTokenObtainPairView,
                CustomObtainAuthToken, CustomDiskardAuthToken, ChangePasswordAPIView,
                     TestEmailSend, ActivationAPIView, ActivationResendAPIView
            )
#from rest_framework.authtoken.views import obtain_auth_token

from rest_framework_simplejwt.views import (TokenRefreshView, TokenVerifyView)


urlpatterns = [
    # registration
    path('registration/', RegistrationApiView.as_view(), name='registration'),
    # test activation

    path('test/confirm/', TestEmailSend.as_view(), name='test'),
    path('activation/confirm/<str:token>', ActivationAPIView.as_view(), name='activation'),
    path('activation/resend/', ActivationResendAPIView.as_view(), name='activation-resend'),
         

    # change password
    path('change_password/', ChangePasswordAPIView.as_view(), name='change_password'),

    # token
    path('token/login/', CustomObtainAuthToken.as_view(), name='token-login'),
    path('token/logout/', CustomDiskardAuthToken.as_view(), name='token-logout'),

    # jwt
    path('jwt/create/', CustomTokenObtainPairView.as_view(), name='jwt-create'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='jwt_refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(), name='jwt_verify'),
]
