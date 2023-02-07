from django.shortcuts import render
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Artist, Disc


class ArtistsView(LoginRequiredMixin, ListView):
    models = Artist
    template_name = 'index.html'
    queryset = Artist.objects.all()
    context_object_name = 'artists'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['artists'] = context['artists'].filter(owner=self.request.user)
        return context


class DetailArtistView(LoginRequiredMixin, ListView):
    model = Disc
    context_object_name = 'discs'
    queryset = Disc.objects.all()
    template_name = 'discs.html'
    
    
    
    
    # será que não é o Disc no model ? disc tem artist, e titles