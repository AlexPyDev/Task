from django.contrib.auth.models import User
from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Roles(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    moderation = models.BooleanField(default=True)


class Permission(BaseModel):
    """Extended User model"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Roles, on_delete=models.SET_NULL, null=True)
