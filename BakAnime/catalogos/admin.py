from django.contrib import admin

from .models import PostImage, Anime, Genero
# Register your models here.

admin.site.register(Anime)
admin.site.register(PostImage)
admin.site.register(Genero)