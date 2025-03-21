from rest_framework import serializers, viewsets
from ...models import Task
from django.urls import reverse


class TaskSerializer(serializers.ModelSerializer):
    absolute_url = serializers.ReadOnlyField(source='get_absolute_url')
    class Meta:
        model = Task
        fields = ['id', 'title', 'owner', 'descriptions', 'image', 'complete',
                  'absolute_url', 'create_date', 'last_update', 'deadline']
    def get_abs_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(reverse('task-detail', args=[obj.pk]))


