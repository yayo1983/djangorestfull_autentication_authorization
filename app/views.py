# articles/views.py

from rest_framework import generics
from .models import Articulo
from .serializers import ArticuloSerializer
from rest_framework.permissions import IsAuthenticated

class ListaArticulos(generics.ListCreateAPIView):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer
    permission_classes = [IsAuthenticated]  # Solo usuarios autenticados

