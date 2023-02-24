from django.test import TestCase
from django.urls import resolve, reverse

from unittest import skip

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
