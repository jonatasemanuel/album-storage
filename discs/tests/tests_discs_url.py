from django.test import TestCase
from django.urls import reverse


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

    def test_search_album_url_is_correct(self):
        url = reverse('search')
        self.assertEqual(url, '/albums/search/')
