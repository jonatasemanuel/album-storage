from django.contrib import admin
from .models import Artist, Disc


@admin.register(Artist)
class ArtistModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'picture')


@admin.register(Disc)
class DiscModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'release')