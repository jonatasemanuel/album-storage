# from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_list_or_404, get_object_or_404, render

from .models import Artist, Disc


def home_view(request):
    return render(request, 'discs/home.html')


def discs_all_discs(request):

    discs = get_list_or_404(
        Disc.objects.order_by('-id')
    )
    context = {'discs': discs}
    return render(request, 'discs/discs.html', context)


def discs_detail_disc(request, slug):

    disc = get_object_or_404(
        Disc, slug=slug)
    context = {'disc': disc}

    return render(request, 'discs/disc-detail.html', context)


def artist_list(request):

    artists = get_list_or_404(
        Artist.objects.order_by('-id')
    )
    context = {'artists': artists}
    return render(request, 'discs/artists.html', context)


def artist_detail(request, slug):

    artist = get_object_or_404(
        Artist, slug=slug)
    context = {'artist': artist}
    return render(request, 'discs/artist-detail.html', context)


def artist_albums(request, artist_slug):
    discs = get_list_or_404(Disc.objects.filter(
        artist__slug=artist_slug
    ).order_by('title'))
    context = {'discs': discs,
               'name': f'{discs[0].artist.name}'}
    return render(request, 'discs/discs.html', context)


def category_albums(request, category_slug):

    discs = get_list_or_404(Disc.objects.filter(
        category__slug=category_slug
    ).order_by('-id')
    )
    context = {'discs': discs,
               'title': f'{discs[0].category.name}'
               }
    return render(request, 'discs/category.html', context)


def search(request):
    search_term = request.GET.get('q', '').strip()
    if not search_term:
        raise Http404()

    discs = Disc.objects.filter(
        Q(
            Q(title__icontains=search_term) |
            Q(artist__name__icontains=search_term) |
            Q(category__name__icontains=search_term)
        )
    ).order_by('-id')

    context = {
        'page_title': f'Search for "{search_term}"',
        'search_term': search_term,
        'discs': discs
    }

    return render(request, 'discs/search.html', context)
