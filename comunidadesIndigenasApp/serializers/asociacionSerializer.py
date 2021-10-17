from comunidadesIndigenasApp.models.asociacion import Asociacion
from rest_framework                            import serializers

class AsociacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asociacion
        fields = ['nombre','texto','departamento']
        
    def to_representation(self,obj):
      asociacion = Asociacion.objects.get(id=obj.id)
      return {
        'nombre' : asociacion.nombre,
        'texto'  : asociacion.texto,
        'departameno' : asociacion.departamento
      }

      