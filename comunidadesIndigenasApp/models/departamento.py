from django.db               import models
from django.db.models.fields import AutoField

class Departamento(models.Model):
    id                = models.AutoField(primary_key=True)
    nombre            = models.CharField(max_length=50)
    numero_resguardos = models.IntegerField(null =False)
    poblacion         = models.IntegerField()
    texto             = models.TextField()