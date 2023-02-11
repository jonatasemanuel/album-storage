from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, TemplateView

from .models import Disc, Artist


class HomeView(TemplateView):
    template_name = 'discs/home.html'


class DiscView(LoginRequiredMixin, ListView):
    model = Disc
    template_name = 'discs/discs.html'
    queryset = Disc.objects.all()
    context_object_name = 'discs'

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['discs'] = context['discs'].filter(owner=self.request.user).order_by('artist')
        return context


class DiscDetail(LoginRequiredMixin, DetailView):
    
    model = Disc
    template_name = 'discs/disc-detail.html'
    
    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        return qs.filter(owner=self.request.user)
    
    
class ArtistsView(LoginRequiredMixin, ListView):
    models = Artist
    template_name = 'discs/artists.html'
    queryset = Artist.objects.all()
    context_object_name = 'artists'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['artists'] = context['artists'].filter(owner=self.request.user)
        return context


class ArtistDetail(LoginRequiredMixin, DetailView):
    model = Artist
    template_name = 'discs/artist-detail.html'
    
    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        return qs.filter(owner=self.request.user)