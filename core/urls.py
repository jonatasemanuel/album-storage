from django.urls import path
from .views import ArtistsView, DetailArtistView


urlpatterns = [
    path('', ArtistsView.as_view(), name='index'),
    path('<int:pk>/discs', DetailArtistView.as_view(), name='discs'),
]


