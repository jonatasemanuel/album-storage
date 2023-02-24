from django.core.exceptions import ValidationError

from django.test import TestCase
from discs.models import Artist, Category, Disc


class DiscModelTest(TestCase):

    def test_disc_category_model_string_representation_is_name_field(self, name='Category'):
        category = Category.objects.create(name=name)

        self.assertEqual(
            str(category),
            category.name
        )

    def test_disc_category_model_name_max_length_is_65_chars(self):
        category = Category.objects.create()
        category.name = 'A' * 66
        with self.assertRaises(ValidationError):
            category.full_clean()

    # def test_disc_model_string_representation_is_name_field(self, title='Disc'):
    #     disc = Disc.objects.create(title=title)

    #     self.assertEqual(
    #         str(disc),
    #         disc.title
    #     )

    # def test_disc_model_name_max_length_is_65_chars(self):
    #     disc = Disc.objects.create()
    #     disc.name = 'A' * 66
    #     with self.assertRaises(ValidationError):
    #         disc.full_clean()

    # def test_disc_artist_string_representation_is_name_field(self, name='NameUser'):
    #     artist = Artist.objects.create(name=name)

    #     self.assertEqual(
    #         str(artist),
    #         artist.title
    #     )

    # def test_disc_artist_name_max_length_is_65_chars(self):
    #     artist = Artist.objects.create()
    #     artist.name = 'A' * 66
    #     with self.assertRaises(ValidationError):
    #         artist.full_clean()
