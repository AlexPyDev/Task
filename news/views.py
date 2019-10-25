from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .models import Article
from .form import ArticleForm, PostForm
from profiles.tasks import send_email


def index(request):
    articles = Article.objects.order_by('id').all()
    return render(request, 'news/index.html', {'articles': articles})

@login_required(login_url='/profile/login/')
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.created_by = request.user
            # Set True to cancel moderation if need
            if not request.user.extendeduserdata.role.moderation:
                article.is_published = True
            article.save()
            return redirect('news:index')
    else:
        form = ArticleForm()
    return render(request, 'news/new_article.html', {'form': form})


def article_posts(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    posts = article.posts.order_by('id')
    return render(request, 'news/article_posts.html', {'article': article, 'posts': posts})


@login_required(login_url='/profile/login/')
def reply_article(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.article = article
            post.created_by = request.user
            post.save()
            send_email(article.created_by.email, f"You have reply in article '{article.title}'")
            return redirect('news:article_posts', article_pk=article.pk)
    else:
        form = PostForm()
    return render(request, 'news/reply_article.html', {'form': form, 'article': article})
