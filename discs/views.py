# from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView

from .models import Artist, Disc


class HomeView(TemplateView):
    template_name = 'discs/home.html'


class DiscView(ListView):

    model = Disc
    template_name = 'discs/discs.html'
    queryset = Disc.objects.all()
    context_object_name = 'discs'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['discs'] = context['discs'].filter(
            owner=self.request.user).order_by('-id')
        return context


class DiscDetail(DetailView):

    model = Disc
    template_name = 'discs/disc-detail.html'

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        return qs.filter(owner=self.request.user)

# class DiscArtistCategory(ListView):
#     template_name = 'discs/discs.html'
#     model = Disc
#     context_object_name = 'albums'

#     def get_context_data(self, artist_slug, **kwargs):
#         context=  super().get_context_data(**kwargs)
#         context['albums'] = context['albums'].filter(
#             owner=self.request.user,
#             artist__slug=artist_slug
#         ).order_by('id')
#         return context

# Turn into class based view and add loginrequiredmixin


def artist(request, artist_slug):
    discs = Disc.objects.filter(
        owner=request.user,
        artist__slug=artist_slug
    ).order_by('title')
    context = {'discs': discs}
    return render(request, 'discs/discs.html', context)


def category(request, category_slug):

    discs = get_list_or_404(Disc.objects.filter(
        category__slug=category_slug
    ).order_by('-id')
    )
    context = {'discs': discs,
               'title': f'{discs[0].category.name}'
               }
    return render(request, 'discs/category.html', context)


class ArtistsView(ListView):
    models = Artist
    template_name = 'discs/artists.html'
    queryset = Artist.objects.all()
    context_object_name = 'artists'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['artists'] = context['artists'].filter(owner=self.request.user)
        return context


class ArtistDetail(DetailView):
    model = Artist
    template_name = 'discs/artist-detail.html'

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        return qs.filter(owner=self.request.user)


class UpdateArtistView(UpdateView):

    model = Artist
    template_name = 'discs/artist-form.html'
    fields = '__all__'
    success_url = reverse_lazy('artists')
