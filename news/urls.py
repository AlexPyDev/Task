"""TestTask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from . import views

app_name = 'news'
urlpatterns = [
    path('', views.index, name='index'),
    path('create-article/', views.create_article, name='create_article'),
    path('article/<str:article_pk>/', views.article_posts, name='article_posts'),
    path('article/<str:article_pk>/reply/', views.reply_article, name='reply_article')
]
