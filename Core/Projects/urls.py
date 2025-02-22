from django.urls import path
from .views import HomePageViews, TaskListViews, TaskCreateViews, TaskDetailViews
urlpatterns = [
    path('', HomePageViews.as_view(), name='home'),
    path('tasks/', TaskListViews.as_view(), name='task_list'),
    path('task/create/',TaskCreateViews.as_view(), name='task_create'),
    path('task/<int:pk>/' ,TaskDetailViews.as_view(), name='task_detail'),
]