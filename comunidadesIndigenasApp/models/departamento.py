from django.db import models

class Departamento(models.Model):
    id                              = models.AutoField(primary_key=True)
    nombre                          = models.CharField(max_length=50, unique=True)
    numero_resguardos               = models.IntegerField()
    numero_municipios_con_resguardo = models.IntegerField()
    poblacion                       = models.IntegerField()
    texto                           = models.TextField(blank=True, null=True)