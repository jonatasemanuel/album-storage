from unittest import skip

from django.test import TestCase
from django.urls import resolve, reverse

from discs import views


class CategoryViewsTest(TestCase):

    @skip('wip')
    def test_category_view_returns_status_200_ok(self):
        response = self.client.get(reverse(
            'category', kwargs={'category_slug': 'hip-hop'}
        ))
        self.assertEqual(response.status_code, 200)

    @skip('wip')
    def test_category_view_loads_correct_template(self):
        response = self.client.get(reverse(
            'category', kwargs={'category_slug': 'hip-hop'}
        ))
        self.assertTemplateUsed(response, 'discs/category.html')

    def test_category_view_function_is_correct(self):
        view = resolve(reverse('category',
                               kwargs={'category_slug': 'hip-hop'}))
        self.assertIs(view.func, views.category_albums)

    def test_category_view_return_404_if_no_category_found(self):
        response = self.client.get(
            reverse('category', kwargs={'category_slug': 'batata'})
        )
        self.assertEqual(response.status_code, 404)

    def test_search_uses_correct_view_function(self):
        resolved = resolve(reverse('search'))
        self.assertIs(resolved.func, views.search)

    def test_search_loads_correct_template(self):
        response = self.client.get(reverse('search') + '?q=test')
        self.assertTemplateUsed(response, 'discs/search.html')

    def test_search_raises_404_if_no_search_term(self):
        url = reverse('search')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_recipe_search_term_is_on_page_title_and_escaped(self):
        url = reverse('search') + '?q=<Test>'
        response = self.client.get(url)
        self.assertIn(
            'Search for &quot;&lt;Test&gt;&quot;',
            response.content.decode('utf-8')
        )
