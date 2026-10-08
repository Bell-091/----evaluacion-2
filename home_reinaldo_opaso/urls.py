from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.vista_inicio, name='inicio'),
    path('genero/<str:genero_id>/', views.vista_peliculas_genero, name='peliculas_genero'),
    path('contacto/', views.vista_contacto, name='contacto'),
]
