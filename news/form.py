from django import forms

from .models import Article, Post


class ArticleForm(forms.ModelForm):
    title = forms.CharField(label='Title:')
    message = forms.CharField(label='Message:',
                              widget=forms.Textarea(attrs={'width': "100%", 'cols': 10, 'rows': 8}),
                              max_length=4000)

    class Meta:
        model = Article
        fields = ['title', 'message']


class PostForm(forms.ModelForm):
    message = forms.CharField(label='Message:',
                              widget=forms.Textarea(attrs={'width': "100%", 'cols': 10, 'rows': 8}),
                              max_length=4000)

    class Meta:
        model = Post
        fields = ['message', ]
