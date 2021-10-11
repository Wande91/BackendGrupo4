from comunidadesIndigenasApp.models.resguardo    import Resguardo
from comunidadesIndigenasApp.models.municipio    import Municipio
from comunidadesIndigenasApp.models.asociacion   import Asociacion
from comunidadesIndigenasApp.models.departamento import Departamento
from .asociacionSerializer                       import AsociacionSerializer
from .municipioSerializer                        import MunicipioSerializer
from rest_framework                              import serializers

class ResguardoSerializer(serializers.ModelSerializer):
    asociacion = AsociacionSerializer()
    municipio  = MunicipioSerializer()

    class Meta:
        model  = Resguardo
        fields = ['id', 'nombre', 'poblacion', 'texto', 'asociacion', 'municipio']

        def to_representation(self, obj):
            asociacion   = Asociacion.objects.get(od = obj.asociacion_id)
            resguardo    = Resguardo.objects.get(id=obj.id)
            municipio    = Municipio.objects.get(id=obj.municipio_id)
            departamento = Municipio.objects.get(id=obj.departamento_id)
            return {
                'id'            : resguardo.id,
                'nombre'        : resguardo.nombre,
                'poblacion'     : resguardo.poblacion,
                'texto'          : resguardo.texto,
                'asociacion' : {
                    'id'            : asociacion.id,
                    'nombre'        : asociacion.nombre,
                    'texto'         : asociacion.texto,
                },
                'municipio' : {
                    'id'            : municipio.id,
                    'nombre'        : municipio.nombre,
                    'texto'         : municipio.texto,
                    'departamento'  : {
                        'id'                : departamento.id,
                        'nombre'            : departamento.nombre,
                        'numero_resguardo:' : departamento.numero_resguardos,
                        'poblacion' : departamento.poblacion,
                        'texto'     : departamento.texto
                    }
                }
            }