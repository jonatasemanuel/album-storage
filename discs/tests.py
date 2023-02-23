from django.test import RequestFactory, TestCase
from django.urls import resolve, reverse

from discs import views


class DiscURLsTest(TestCase):

    def test_disc_home_url_is_correct(self):
        url = reverse('home')
        self.assertEqual(url, '/')

    def test_disc_list_url_is_correct(self):
        url = reverse('discs')
        self.assertEqual(url, '/discs/')

    def test_disc_detail_url_is_correct(self):
        url = reverse('disc-detail', kwargs={'slug': 'test'})
        self.assertEqual(url, '/test/')

    def test_artists_url_is_correct(self):
        url = reverse('artists')
        self.assertEqual(url, '/artists/albums/')

    def test_artist_detail_url_is_correct(self):
        url = reverse('artist-detail', kwargs={'slug': 'test'})
        self.assertEqual(url, '/artist/test/')

    def test_artist_albums_url_is_correct(self):
        url = reverse('albums', kwargs={'artist_slug': 'song'})
        self.assertEqual(url, '/artist/albums/song/')

    def test_category_albums_url_is_correct(self):
        url = reverse('category', kwargs={'category_slug': 'rap'})
        self.assertEqual(url, '/albums/category/rap/')


class DiscViewsTest(TestCase):

    def test_discs_home_returns_status_code_200_ok(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_discs_home_loads_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'discs/home.html')

    def test_discs_home_view_function_is_correct(self):
        view = resolve(reverse('home'))
        self.assertIs(view.func, views.home_view)

    def test_discs_all_discs_status_code_200_ok(self):
        response = self.client.get(reverse('discs'))
        self.assertEqual(response.status_code, 200)

    def test_discs_all_discs_loads_correct_template(self):
        response = self.client.get(reverse('discs'))
        self.assertTemplateUsed(response, 'discs/discs.html')

    def test_discs_all_discs_function_is_correct(self):
        view = resolve(reverse('discs'))
        self.assertIs(view.func, views.discs_all_discs)

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

    def test_discs_category_view_function_is_correct(self):
        view = resolve(reverse('category',
                       kwargs={'category_slug': 'hip-hop'}))
        self.assertIs(view.func, views.category_albums)

    def test_discs_category_view_return_404_if_no_discs_found(self):
        response = self.client.get(
            reverse('category', kwargs={'category_slug': 'batata'})
        )
        self.assertEqual(response.status_code, 404)

    def test_discs_artist_view_returns_status_code_200_ok(self):
        response = self.client.get(reverse('artists'))
        self.assertEqual(response.status_code, 200)

    def test_discs_artist_view_loads_correct_template(self):
        response = self.client.get(reverse('artists'))
        self.assertTemplateUsed(response, 'discs/artists.html')

    def test_discs_artists_template_shows_no_artists_found_if_no_artists(self):
        response = self.client.get(reverse('artists'))
        self.assertIn(
            'algo',
            response.content.decode('utf-8')
        )

    def test_discs_artists_view_function_is_correct(self):
        view = resolve(reverse('artists'))
        self.assertIs(view.func, views.artist_list)

    def test_discs_artists_detail_view_is_correct(self):
        view = resolve(reverse('artist-detail',
                               kwargs={'artist_slug': 'bk'}))
        self.assertIs(view.func, views.artist_detail)

    def test_discs_artist_view_returns_404_if_no_artists_found(self):
        response = self.client.get(
            reverse('artists', kwargs={'artist_slug': 'batata'})
        )
        self.assertEqual(response.status_code, 404)
