from comunidadesIndigenasApp.models.departamento import Departamento
from rest_framework                              import serializers

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = ['nombre', 'numero_resguardos', 'poblacion', 'texto']
    
    def to_representation(self,obj):
      departamento = Departamento.objects.get(id=obj.id)
      return {
        'id'                : departamento.id,
        'nombre'            : departamento.nombre,
        'numero_resguardos' : departamento.numero_resguardos,
        'poblacion'         : departamento.poblacion,
        'texto'             : departamento.texto
      }