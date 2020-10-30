from django.shortcuts import render, get_object_or_404, redirect
from .models import PostImage, Anime, Genero
# Create your views here.


def index(request):
    num_blog = Anime.objects.all()
    
    return render(
        request,
        'index.html',
        context={'num_blog':num_blog}
    )


def blog(request):
    num_blog = Anime.objects.all()

    return render(
        request,
        'blog.html',
        context={'num_blog':num_blog}
    )
    
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import generic

class AnimeDetalles(generic.DetailView):
    model = Anime    
