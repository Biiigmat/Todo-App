from django.urls import path
from django.urls import include

from .views import LoginUserView, user_logout_view, UserRegisterView

app_name = 'accounts'

urlpatterns = [
    # path('login/', LoginUserView.as_view(), name='user_login'),
    # path('logout/', user_logout_view, name='user_logout'),
    # path('register/', UserRegisterView.as_view(), name='user_register'),
    path('', include('django.contrib.auth.urls')),
    path('api/v1/', include('Accounts.api.v1.urls')),
]