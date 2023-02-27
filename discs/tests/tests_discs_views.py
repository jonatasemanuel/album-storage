from django.test import TestCase
from django.urls import resolve, reverse

from unittest import skip

from discs import views


class DiscViewsTest(TestCase):

    def test_home_returns_status_code_200_ok(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_loads_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'discs/home.html')

    def test_home_view_function_is_correct(self):
        view = resolve(reverse('home'))
        self.assertIs(view.func, views.home_view)

    def test_discs_all_discs_function_is_correct(self):
        view = resolve(reverse('discs'))
        self.assertIs(view.func, views.discs_all_discs)

    @skip('wip')
    def test_discs_all_discs_status_code_200_ok(self):
        response = self.client.get(reverse('discs'))
        self.assertEqual(response.status_code, 200)

    @skip('wip')
    def test_discs_all_discs_loads_correct_template(self):
        response = self.client.get(reverse('discs'))
        self.assertTemplateUsed(response, 'discs/discs.html')

    def test_discs_all_template_shows_no_artists_found_if_no_artists(self):
        response = self.client.get(reverse('discs'))
        self.assertIn(
            'Not Found',
            response.content.decode('utf-8')
        )

    def test_discs_detail_view_function_is_correct(self):
        view = resolve(reverse('disc-detail', kwargs={'slug': 'batata'}))
        self.assertIs(view.func, views.discs_detail_disc)

    def test_discs_detail_view_returns_404_if_no_discs_found(self):
        response = self.client.get(
            reverse('disc-detail', kwargs={'slug': 'batata'})
        )
        self.assertEqual(response.status_code, 404)
