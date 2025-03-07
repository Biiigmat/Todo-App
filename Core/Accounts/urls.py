from django.urls import path
from .views import LoginUserView, user_logout_view, UserRegisterView

urlpatterns = [
    path('login/', LoginUserView.as_view(), name='user_login'),
    path('logout/', user_logout_view, name='user_logout'),
    path('register/', UserRegisterView.as_view(), name='user_register'),
]