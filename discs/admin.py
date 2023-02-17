from django.contrib import admin
from .models import Disc, Artist, Category


@admin.register(Artist)
class ArtistModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':  ('name',)}
    list_display = ('name', 'picture')


@admin.register(Disc)
class DiscModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':  ('title',)}
    list_display = ('title', 'artist', 'release')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':  ('name',)}
    fields = ['name', 'slug']
