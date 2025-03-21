from rest_framework import serializers, viewsets
from ...models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'owner', 'descriptions', 'image', 'complete',
                  'create_date', 'last_update', 'deadline']

