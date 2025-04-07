from django.urls import path
from .views import TaskListCreateAPIView, TaskDetailUpdateDeleteView
# from rest_framework.routers import DefaultRouter
# from .views import TaskViewSet
# app_name = 'api_v1'
# router = DefaultRouter()
# router.register('task', TaskViewSet, basename='task')
# urlpatterns = router.urls


app_name = 'api_v1'

urlpatterns = [
    path('task_list/', TaskListCreateAPIView.as_view()),
    path('task/<int:pk>/', TaskDetailUpdateDeleteView.as_view(), name='task_detail'),
]