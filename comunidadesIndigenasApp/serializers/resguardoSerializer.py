from comunidadesIndigenasApp.models.resguardo    import Resguardo
from comunidadesIndigenasApp.models.municipio    import Municipio
from comunidadesIndigenasApp.models.asociacion   import Asociacion
from comunidadesIndigenasApp.models.departamento import Departamento
from rest_framework                              import serializers

class ResguardoSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Resguardo
        fields = ['id', 'nombre', 'poblacion', 'texto', 'asociacion']

        def to_representation(self, obj):
            resguardo    = Resguardo.objects.get(id=obj.id)
            asociacion   = Asociacion.objects.get(id = obj.asociacion.id)
            municipio    = Municipio.objects.get(id=obj.asociacion.municipio.id)
            departamento = Municipio.objects.get(id=obj.asociacion.municipio.departamento.id)
            return {
                'id'            : resguardo.id,
                'nombre'        : resguardo.nombre,
                'poblacion'     : resguardo.poblacion,
                'texto'         : resguardo.texto,
                'asociacion' : {
                    'id'     : asociacion.id,  
                    'nombre' : asociacion.nombre,
                    'texto'  : asociacion.texto,
                },
                'municipio' : {
                    'nombre': municipio.nombre,
                    'texto' : municipio.texto,
                    'departamento'  : {
                        'nombre' : departamento.nombre,
                        'poblacion': departamento.poblacion
                    }
                }
            }