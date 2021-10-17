from django.db     import models
from .departamento import Departamento

class Municipio(models.Model):
    id              = models.AutoField(primary_key=True)
    nombre          = models.CharField(max_length=50)
    texto           = models.TextField(blank=True, null=True)
    departamento= models.ForeignKey(Departamento, related_name='departamento', on_delete=models.CASCADE)
