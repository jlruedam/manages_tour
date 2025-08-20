from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import viewsets
from rest_framework.response import Response

from sales.models import Client
from cities_light.models import Country, City
from .serializers import ClientSerializer, CitySerializer

# Create your views here.
class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # Filtros exactos
    filterset_fields = ["name", "country", "region"]
    
    # Búsqueda parcial
    search_fields = ["name"]
    
    # Ordenación
    ordering_fields = ["name", "country"]
    ordering = ["name"]