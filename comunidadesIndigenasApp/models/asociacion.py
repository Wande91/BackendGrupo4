from django.db import models

class Asociacion(models.Model):
    id     = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150)
    texto  = models.TextField(blank=True, null=True)