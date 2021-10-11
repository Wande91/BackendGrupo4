from django.db    import models
from .asociacion  import Asociacion
from .municipio   import Municipio

class Resguardo(models.Model):
    id         = models.AutoField(primary_key=True)
    nombre     = models.CharField(max_length=60)
    poblacion  = models.IntegerField()
    texto      = models.TextField()
    asociacion = models.ForeignKey(Asociacion, related_name='asociacion', on_delete=models.CASCADE)
    municipio  = models.ForeignKey(Municipio, related_name='municipio', on_delete=models.CASCADE)