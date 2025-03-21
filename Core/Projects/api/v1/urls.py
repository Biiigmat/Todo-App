from django.urls import path
from .views import TaskListCreateAPIView, TaskDetailUpdateDeleteView
from rest_framework.routers import DefaultRouter

app_name = 'api_v1'


urlpatterns = [
    path('task_list/', TaskListCreateAPIView.as_view(), name='task_list'),
    path('task/<int:pk>/', TaskDetailUpdateDeleteView.as_view(), name='task_detail'),
]