from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Article


'''DB TESTS'''


class ArticleModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(username='test', password='test1234')
        Article.objects.create(created_by=user, title='Test article', message='Test message')

    def test_title_label(self):
        article = Article.objects.get(title='Test article')
        field_label = article._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_message_label(self):
        article = Article.objects.get(title='Test article')
        field_label = article._meta.get_field('message').verbose_name
        self.assertEqual(field_label, 'message')

    def test_is_published_label(self):
        article = Article.objects.get(title='Test article')
        field_label = article._meta.get_field('is_published').verbose_name
        self.assertEqual(field_label, 'is published')

    def test_created_by_label(self):
        article = Article.objects.get(title='Test article')
        field_label = article._meta.get_field('created_by').verbose_name
        self.assertEqual(field_label, 'created by')

    def test_updated_by_label(self):
        article = Article.objects.get(title='Test article')
        field_label = article._meta.get_field('updated_by').verbose_name
        self.assertEqual(field_label, 'updated by')

    def test_created_at_label(self):
        article = Article.objects.get(title='Test article')
        field_label = article._meta.get_field('created_at').verbose_name
        self.assertEqual(field_label, 'created at')

    def test_modified_at_label(self):
        article = Article.objects.get(title='Test article')
        field_label = article._meta.get_field('modified_at').verbose_name
        self.assertEqual(field_label, 'modified at')

    def test_title_max_length(self):
        article = Article.objects.get(title='Test article')
        max_length = article._meta.get_field('title').max_length
        self.assertEqual(max_length, 128)


''' VIEWS TESTS '''


class IndexViewTests(TestCase):

    def test_url_exists_at_desired_location(self):
        url = '/news/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_url_accessible_by_name(self):
        url = reverse('news:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        url = reverse('news:index')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'news/index.html')


class NikkorLensesViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(username='test', password='test1234')
        Article.objects.create(created_by=user, title='Test article', message='Test message')

    def test_url_exists_at_desired_location(self):
        url = '/news/article/2/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_url_accessible_by_name(self):
        url = reverse('news:article_posts', kwargs={'article_pk': 2})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_url_uses_correct_template(self):
        url = reverse('news:article_posts', kwargs={'article_pk': 2})
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'news/article_posts.html')

    def test_404(self):
        Article.objects.filter(title='Test article').delete()
        url = reverse('news:article_posts', kwargs={'article_pk': 2})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
