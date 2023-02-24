from django.test import TestCase
from django.urls import resolve, reverse

from unittest import skip

from discs import views


class ArtistViewsTest(TestCase):

    @skip('wip')
    def test_artist_view_returns_status_code_200_ok(self):
        response = self.client.get(reverse('artists'))
        self.assertEqual(response.status_code, 200)

    @skip('wip')
    def test_artist_view_loads_correct_template(self):
        response = self.client.get(reverse('artists'))
        self.assertTemplateUsed(response, 'discs/artists.html')

    def test_artists_template_shows_no_artists_found_if_no_artists(self):
        response = self.client.get(reverse('artists'))
        self.assertIn(
            'Not Found',
            response.content.decode('utf-8')
        )

    def test_artists_view_function_is_correct(self):
        view = resolve(reverse('artists'))
        self.assertIs(view.func, views.artist_list)

    def test_artists_detail_view_is_correct(self):
        view = resolve(reverse('artist-detail',
                               kwargs={'slug': 'batata'}))
        self.assertIs(view.func, views.artist_detail)

    def test_artist_view_returns_404_if_no_artists_found(self):
        response = self.client.get(
            reverse('artist-detail', kwargs={'slug': 'batata'})
        )
        self.assertEqual(response.status_code, 404)

    def test_artist_albums_view_is_correct(self):
        view = resolve(reverse(
            'albums', kwargs={'artist_slug': 'bk'}
        ))
        self.assertIs(view.func, views.artist_albums)

    def test_artist_albums_returns_404_if_no_albums_found(self):
        response = self.client.get(
            reverse('albums', kwargs={'artist_slug': 'batata'})
        )
        self.assertEqual(response.status_code, 404)
