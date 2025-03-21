from django.db import models
from Accounts.models import User
from django.urls import reverse


class Task (models.Model):
    title = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='users/', null=True, blank=True)
    descriptions = models.TextField()
    complete = models.BooleanField(default=False)

    create_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse("projects:api_v1:task-detail", args=[self.id])

