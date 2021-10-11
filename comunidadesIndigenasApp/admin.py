from django.contrib                              import admin
from comunidadesIndigenasApp.models.asociacion   import Asociacion
from comunidadesIndigenasApp.models.departamento import Departamento
from comunidadesIndigenasApp.models.municipio    import Municipio
from comunidadesIndigenasApp.models.resguardo    import Resguardo
# Register your models here.


admin.site.register(Asociacion)
admin.site.register(Departamento)
admin.site.register(Municipio)
admin.site.register(Resguardo)

