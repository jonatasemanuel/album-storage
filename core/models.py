from django.contrib.auth.models import User

from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='pictures/%Y/%m/')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    
    def __str__(self) -> str:
        return self.name


class Disc(models.Model):
    title = models.CharField(max_length=50)
    artist = models.ForeignKey(Artist, on_delete=models.DO_NOTHING)
    release = models.DateField()
    artwork = models.ImageField(upload_to='artworks/%Y/%m/')


    def __str__(self) -> str:
        return self.title
