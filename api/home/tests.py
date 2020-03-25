from django.test import TestCase
from django.urls import resolve
from .views import HomePageView


class AppsTest(TestCase):

    def test_app_name(self):
        from .apps import HomeConfig

        self.assertEqual(HomeConfig.name, 'home')


class ViewsTest(TestCase):

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')

        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<!DOCTYPE html>'))
        self.assertIn('<h1>Under Construction</h1>', html)
        self.assertTrue(html.strip().endswith('</html>'))

        self.assertTemplateUsed(response, 'home.html')


class UrlsTest(TestCase):

    def test_root_url_name(self):
        resolver = resolve('/')
        self.assertEqual(resolver.view_name, 'home')

    def test_root_url_resolves_to_home_page_view(self):
        resolver = resolve('/')
        self.assertEqual(resolver.func.view_class, HomePageView)
