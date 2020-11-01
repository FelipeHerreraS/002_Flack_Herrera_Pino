from django.db import models
from django.urls import reverse
import uuid 

# Create your models here.

class Genero(models.Model):
    name = models.CharField('Nombre', max_length=30,null=False)
    description = models.TextField(max_length=800, null=False)

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('genre-detail', args=[str(self.id)])

    def __str__(self):
        return self.name

class Anime(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    tituloPag = models.TextField(max_length=200, null=True)
    sinopsis = models.TextField(max_length=500, null=True)
    image = models.ImageField(upload_to='images/', blank=True)
    capitulos = models.CharField(max_length=20, null=True)
    duracion = models.CharField(max_length=20, null=True)
    generos = models.ManyToManyField('Genero')
    año = models.IntegerField(null=True)
    peso = models.CharField(max_length=20, null=True)
    subtitulos = models.CharField(max_length=200, null=True)
    calidad = models.CharField(max_length=200, null=True)
    formato = models.CharField(max_length=30, null=True)
    tipo = models.CharField(max_length=20, null=True)
    desnudos = models.CharField(max_length=2, null=True)
    censura = models.CharField(max_length=2, null=True)

    def __str__(self):
        return self.tituloPag

    def get_absolute_url(self):
        return reverse('anime-detail', args=[str(self.id)])

class PostImage(models.Model):
    post = models.ForeignKey(Anime, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/')
    
    def __str__(self):
        return self.post.tituloPag