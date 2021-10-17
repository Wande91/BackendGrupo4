from django.db                       import models
from django.db.models.fields.related import ForeignKey
from .municipio                      import Municipio

from comunidadesIndigenasApp.models.municipio import Municipio

class Asociacion(models.Model):
    id     = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150, unique=True)
    municipio = ForeignKey(Municipio,related_name='municipio', on_delete=models.CASCADE)
    texto  = models.TextField(blank=True, null=True)

    