from comunidadesIndigenasApp.models.resguardo    import Resguardo
from comunidadesIndigenasApp.models.municipio    import Municipio
from comunidadesIndigenasApp.models.asociacion   import Asociacion
from comunidadesIndigenasApp.models.departamento import Departamento
from rest_framework                              import serializers

class ResguardoSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Resguardo
        fields = ['id', 'nombre', 'poblacion', 'texto', 'asociacion_id', 'municipio_id']

        def to_representation(self, obj):
            asociacion   = Asociacion.objects.get(id = obj.asociacion_id)
            resguardo    = Resguardo.objects.get(id=obj.id)
            municipio    = Municipio.objects.get(id=obj.municipio_id)
            departamento = Municipio.objects.get(id=obj.departamento_id)
            return {
                'id'            : resguardo.id,
                'nombre'        : resguardo.nombre,
                'poblacion'     : resguardo.poblacion,
                'texto'         : resguardo.texto,
                'asociacion_id' : {
                    'id'     : asociacion.id,  
                    'nombre' : asociacion.nombre,
                    'texto'  : asociacion.texto,
                },
                'municipio_id' : {
                    'id'               : municipio.id,
                    'nombre'           : municipio.nombre,
                    'departamento_id'  : {
                        'id'     : departamento.id,
                        'nombre' : departamento.nombre
                    }
                }
            }