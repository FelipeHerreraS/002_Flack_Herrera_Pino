from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('blog/', views.blog, name='blog'),
    path('blog/<str:pk>', views.AnimeDetalles.as_view(), name='blog-detail'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
]