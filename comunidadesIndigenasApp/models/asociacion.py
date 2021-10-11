from django.db                  import models
from django.contrib.auth.models import AbstractBaseUser, PermissionManager, BaseUserManager

class Asociacion(models.Model):
    id     = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150)
    texto  = models.TextField()