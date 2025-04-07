from rest_framework import serializers, viewsets
from ...models import Task
from django.urls import reverse


class TaskSerializer(serializers.ModelSerializer):
    absolute_url = serializers.ReadOnlyField(source='get_absolute_url')
    class Meta:
        model = Task
        fields = ['id', 'title', 'owner', 'descriptions', 'image', 'complete',
                  'absolute_url', 'create_date', 'last_update', 'deadline',]
        read_only_fields = ['owner']





