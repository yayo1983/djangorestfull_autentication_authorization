# articles/views.py

from rest_framework import generics
from .models import Articulo
from .serializers import ArticuloSerializer

class ListaArticulos(generics.ListCreateAPIView):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer

