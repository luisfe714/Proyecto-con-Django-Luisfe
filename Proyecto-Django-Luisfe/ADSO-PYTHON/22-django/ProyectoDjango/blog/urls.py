from django.urls import path
from . import views

urlpatterns = [
    path('articulos/', views.list, name="list_articles"),#Cuando encuentra la ruta inicio
]