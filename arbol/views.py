from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import PredioSerializer
from .serializers import DireccionSerializer
from .serializers import FotoSerializer
from .models import Predio
from .models import direccion
from .models import foto


def index(request):
    return HttpResponse("hola mundo")

class PredioViewSet(viewsets.ModelViewSet):
    queryset= Predio.objects.all()
    serializer_class=PredioSerializer

class DireccionViewSet(viewsets.ModelViewSet):
    queryset= direccion.objects.all()
    serializer_class=DireccionSerializer

class FotoViewSet(viewsets.ModelViewSet):
    queryset= foto.objects.all()
    serializer_class=FotoSerializer
# Create your views here.
