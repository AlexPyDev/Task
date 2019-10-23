from django.contrib.auth.models import User
from django.db import models


class BaseModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Article(BaseModel):
    title = models.CharField(max_length=256)
    content = models.TextField()
    is_published = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
