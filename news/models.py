from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Article(BaseModel):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='+')
    title = models.CharField(max_length=128)
    message = models.TextField()
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Post(BaseModel):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='posts')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='+')
    message = models.CharField(max_length=4000)

    def __str__(self):
        return self.message
