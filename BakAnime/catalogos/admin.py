from django.contrib import admin

from .models import PostImage, Anime, Genero
# Register your models here.

#admin.site.register(Anime)
#admin.site.register(PostImage)  
admin.site.register(Genero)
#admin.site.register(Peticiones)

class PostImageAdmin(admin.StackedInline):
    model = PostImage

@admin.register(Anime)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

    class Meta:
       model = Anime

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass