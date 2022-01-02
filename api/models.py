from django.contrib.auth.models import AbstractUser
from django.db import models


class Users(AbstractUser):
    isProjectManager = models.BooleanField(default=False)


class Projects(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='projects')
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField()
    start_date = models.DateTimeField()
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
