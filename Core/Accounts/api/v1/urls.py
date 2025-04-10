from django.urls import path, include
from .views import RegistrationApiView, CustomAuthToken
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
    path('registration',RegistrationApiView.as_view(),name='registration'),
    path('token/login', CustomAuthToken.as_view(), name='token-login'),
]
