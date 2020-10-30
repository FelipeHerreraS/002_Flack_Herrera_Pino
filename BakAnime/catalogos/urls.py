from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('blog/', views.blog, name='blog'),
    path('blog/<str:pk>', views.AnimeDetalles.as_view(), name='anime-detail'),
]

urlpatterns += [
    path('',views.index,name='index'),
    path('blog/', views.blog, name='blog'),
    path('blog/<str:pk>', views.AnimeDetalles.as_view(), name='anime-detail'),
]