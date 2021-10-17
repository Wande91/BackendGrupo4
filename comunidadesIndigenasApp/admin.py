from django.contrib       import admin
from .models.asociacion   import Asociacion
from .models.departamento import Departamento
from .models.municipio    import Municipio
from .models.resguardo    import Resguardo
from .models.user         import User

admin.site.register(Asociacion)
admin.site.register(Departamento)
admin.site.register(Municipio)
admin.site.register(Resguardo)
admin.site.register(User)

