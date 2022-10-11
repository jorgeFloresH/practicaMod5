from email.policy import default
from pyexpat import model
#from typing_extensions import Required
from django.db import models
from django.conf import settings
from .validators import validar_codcat
from .validators import validar_distrito
from .validators import validar_subdistrito
# Create your models here.
class tipoArbol(models.Model):
    nombreTipo=models.CharField(max_length=100)

    def __str__(self):
        return self.nombreTipo




class foto(models.Model):
    url=models.URLField(max_length=200)
    nombre=models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Predio(models.Model):
    latidud=models.FloatField()
    longitud=models.FloatField()
    distrito=models.IntegerField(default=0, validators=[validar_distrito,])
    subdistrito=models.IntegerField(default=0, validators=[validar_subdistrito,])
    codigoCatastral=models.CharField(max_length=100, validators=[validar_codcat,])

class direccion(models.Model):
    calle=models.CharField(max_length=100)
    nro=models.CharField(max_length=100)
    zona=models.CharField(max_length=100)

class Arbol(models.Model):
    nombre=models.CharField(max_length=100)
    tipo=models.CharField(max_length=100)
    codigoArbol=models.CharField(max_length=100, unique=True)
    tipoArbol=models.ForeignKey(tipoArbol, on_delete=models.CASCADE)
    fotoArbol=models.ForeignKey(foto, on_delete=models.CASCADE) 
    predioArbol=models.ForeignKey(Predio, on_delete=models.CASCADE)
    direccionArbol=models.ForeignKey(direccion, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre