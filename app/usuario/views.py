from django.shortcuts import render

from rest_framework import generics

from .models import Persona
from .serializers import *


class PersonaListCreateView(generics.ListCreateAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer


class AcudienteListCreateView(generics.ListCreateAPIView):
    queryset = Acudiente.objects.all()
    serializer_class = AcudienteSerializer


class TelefonoListCreateView(generics.ListCreateAPIView):
    queryset = Telefono.objects.all()
    # queryset = Telefono.objects.filter(tipo=Telefono.TIPO_MOVIL)
    # queryset = Telefono.objects.filter(tipo=Telefono.TIPO_MOVIL).order_by('numero')
    serializer_class = TelefonoSerializer
