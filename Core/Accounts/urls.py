from django.urls import path
from .views import LoginUserView, user_logout_view

urlpatterns = [
    path('login/', LoginUserView.as_view(), name='user_login'),
    path('logout/', user_logout_view, name='user_logout'),
]