from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_view, name='home'),

    path('discs/', views.discs_all_discs,  name='discs'),

    path('albums/search/', views.search, name='search'),

    path('<slug:slug>/', views.discs_detail_disc, name='disc-detail'),

    path('artists/albums/', views.artist_list, name='artists'),

    path('artist/<slug:slug>/', views.artist_detail, name='artist-detail'),

    path('artist/albums/<slug:artist_slug>/',
         views.artist_albums, name='albums'),

    path('albums/category/<slug:category_slug>/',
         views.category_albums, name='category'),
]
