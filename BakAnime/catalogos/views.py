from django.shortcuts import render, get_object_or_404, redirect
from .models import PostImage, Anime, Genero
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect 
from . forms import Peticiones
# Create your views here.

def registerPage(request):
    context= {}
    return render(request, 'register.html', context)

def loginPage(request):
    context = {}
    return render(request, 'login.html', context)

def index(request):
    last = Anime.objects.all()
    return render(request, 'index.html', context={'last':last})

def blog(request, id):
    num_blog = Anime.objects.all()
    photos = PostImage.objects.filter(num_blog=num_blog)

    return render(
        request,
        'blog-detail.html',
        context={'num_blog':num_blog, 'photos':photos}
    )

def genre(request):
    gen = Genero.objects.all()

    return render(
        request,
        'genero.html'
    )
    
def peticiones(request):
    if request.method == "POST":
        form = Peticiones(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = Peticiones()
        return render(request, 'peticiones.html', {'form': form})


class AnimeDetalles(generic.DetailView):
    model = Anime    

class AnimeListView(generic.ListView):
    model = Anime
    template_name = 'templates/catalogos/anime_list.html'
    context_object_name = 'animes'
    queryset = Anime.objects.all()[:2]

    paginate_by = 4
