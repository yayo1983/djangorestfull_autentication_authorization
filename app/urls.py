from django.urls import path
from .views import ListaArticulos

urlpatterns = [
    path('articulos/', ListaArticulos.as_view(), name='lista_articulos'),
]
