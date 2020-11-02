from django.shortcuts import render, get_object_or_404, redirect
from .models import PostImage, Anime, Genero, Peticiones
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from . forms import PeticionesForm
# Create your views here.

def registerPage(request):
    context= {}
    return render(request, 'register.html', context)

def loginPage(request):
    context = {}
    return render(request, 'login.html', context)

def index(request):
    last = Anime.objects.all().order_by('id')[:2]
    return render(request, 'index.html', context={'last':last})

def blog(request):
    num_blog = Anime.objects.all()

    last = Anime.objects.all().order_by('time')[:2]
    return render(
        request,
        'blog-detail.html',
        context={'num_blog':num_blog, 'last':last}
    )

def genre(request):
    gen = Genero.objects.all()

    return render(
        request,
        'genero.html'
    )


def peticionesR(request):
    if request.method == "POST":
        form = PeticionesForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return HttpResponse("<h1>Tu pedido ha sido Recibido, Muchas Gracias!! <3</h1>")
    else:
        form = PeticionesForm()
        return render(request, 'peticiones.html', {'form': form})

class AnimeDetalles(generic.DetailView):
    model = Anime    

class AnimeListView(generic.ListView):
    model = Anime
    paginate_by = 5
