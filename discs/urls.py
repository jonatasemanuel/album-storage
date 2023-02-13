from django.urls import path
from .views import DiscView, ArtistsView, DiscDetail, ArtistDetail, HomeView, artist

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('discs', DiscView.as_view(), name='discs'),
    path('albums/<slug:artist_slug>/', artist, name='albums'),    
    path('artists', ArtistsView.as_view(), name='artists'),
    path('<slug:slug>', DiscDetail.as_view(), name='disc-detail'),
    path('artist/<slug:slug>', ArtistDetail.as_view(), name='artist-detail')
]
