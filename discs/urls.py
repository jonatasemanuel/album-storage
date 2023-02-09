from django.urls import path
from .views import DiscView, ArtistsView, DiscDetail, ArtistDetail

urlpatterns = [
    path('discs', DiscView.as_view(), name='discs'),
    path('artists', ArtistsView.as_view(), name='artists'),
    path('<slug:slug>', DiscDetail.as_view(), name='disc-detail'),
    path('artist/<int:pk>', ArtistDetail.as_view(), name='artist-detail')
]
