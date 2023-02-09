from django.contrib import admin
from .models import Disc, Artist


@admin.register(Artist)
class ArtistModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'picture')
    

@admin.register(Disc)
class DiscModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':  ('title',)}
    list_display = ('title', 'artist', 'release')
