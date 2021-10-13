from comunidadesIndigenasApp.models.asociacion import Asociacion
from rest_framework                            import serializers

class AsociacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asociacion
        fields = ['nombre','texto']
        
    def to_representation(self,obj):
      asociación = Asociacion.objects.get(id=obj.id)
      return {
        'nombre' : asociacion.nombre,
        'texto'  : asociacion.texto
      }