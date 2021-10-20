from django.db    import models
from .asociacion  import Asociacion
from .municipio   import Municipio

class Resguardo(models.Model):
    id            = models.IntegerField(primary_key=True)
    nombre        = models.CharField(max_length=60)
    poblacion     = models.IntegerField() 
    texto         = models.TextField(blank=True, null=True)
    asociacion    = models.ForeignKey(Asociacion, related_name='asociacion', on_delete=models.CASCADE)