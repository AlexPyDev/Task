from django.contrib import admin

# Register your models here.
from .models import Article, Post

admin.site.register([Article, Post])
