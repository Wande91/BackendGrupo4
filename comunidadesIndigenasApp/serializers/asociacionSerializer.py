from rest_framework                               import serializers
from comunidadesIndigenasApp.models.asociacion    import Asociacion
from comunidadesIndigenasApp.models.departamento  import Departamento
from comunidadesIndigenasApp.models.municipio     import Municipio


class AsociacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asociacion
        fields = ['nombre','texto','municipio']

    def to_representation(self,obj):
      asociacion = Asociacion.objects.get(id=obj.id)
      municipio = Municipio.objects.get(id=obj.municipio.id)
      departamento = Departamento.objects.get(id=obj.municipio.departamento.id)
      return {
        'nombre'    : asociacion.nombre,
        'texto'     : asociacion.texto,
        'municipio' : {
          'municipio_id' : municipio.id,
          'nombre'  : municipio.nombre
        },
        'departamento':{
          'departamento_id' : departamento.id,
          'nombre' : departamento.nombre
        }
      }
    

      