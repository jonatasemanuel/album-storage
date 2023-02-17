from django.urls import path, re_path

from .views import (ArtistDetail, ArtistsView, DiscDetail, DiscView, HomeView,
                    UpdateArtistView, artist, category)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    path('discs/', DiscView.as_view(), name='discs'),

    path('artists/', ArtistsView.as_view(), name='artists'),

    path('<slug:slug>/', DiscDetail.as_view(), name='disc-detail'),

    path('artist/<slug:slug>/', ArtistDetail.as_view(), name='artist-detail'),

    path('edit-artist/<int:pk>/', UpdateArtistView.as_view(),
         name='edit-artist'),

    path('artist/albums/<slug:artist_slug>/', artist, name='albums'),

    path('albums/category/<slug:category_slug>/',
         category, name='category'),

]
