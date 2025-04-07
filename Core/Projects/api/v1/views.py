from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from .serializer import TaskSerializer
from ...models import Task
from rest_framework import viewsets


class TaskListCreateAPIView(ListCreateAPIView):
    """
    API endpoint that shows all tasks
    """
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)


class TaskDetailUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    lookup_field = 'pk'


# class TaskViewSet(viewsets.ModelViewSet):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
#

