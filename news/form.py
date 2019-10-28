from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Article, Post


class ArticleForm(forms.ModelForm):
    title = forms.CharField(label='Title:')
    message = forms.CharField(label='Message:',
                              widget=CKEditorUploadingWidget(),
                              max_length=4000)

    class Meta:
        model = Article
        fields = ['title', 'message']


class PostForm(forms.ModelForm):
    message = forms.CharField(label='',
                              widget=CKEditorUploadingWidget(),
                              max_length=4000)

    class Meta:
        model = Post
        fields = ['message', ]
