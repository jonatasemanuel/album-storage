from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(null=True)

    def __str__(self) -> str:
        return self.name


class Artist(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(null=True)
    picture = models.ImageField(upload_to='pictures/%Y/%m/')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class Disc(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(null=True)
    release = models.DateField()
    artwork = models.ImageField(upload_to='artworks/%Y/%m/')
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 null=True, blank=True, default=None)

    def __str__(self) -> str:
        return self.title
