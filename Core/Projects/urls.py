from django.urls import path
from .views import HomePageViews, TaskListViews, TaskCreateViews, TaskDetailViews, TaskUpdateViews, TaskDeleteViews
urlpatterns = [
    path('', HomePageViews.as_view(), name='home'),
    path('tasks/', TaskListViews.as_view(), name='task_list'),
    path('task/create/', TaskCreateViews.as_view(), name='task_create'),
    path('task/<int:pk>/', TaskDetailViews.as_view(), name='task_detail'),
    path('task/<int:pk>/update/', TaskUpdateViews.as_view(), name='task_update'),
    path('task/<int:pk>/delete/', TaskDeleteViews.as_view(), name='task_delete'),
]