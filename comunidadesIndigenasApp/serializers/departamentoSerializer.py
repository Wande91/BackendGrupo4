from comunidadesIndigenasApp.models.departamento import Departamento
from rest_framework                              import serializers

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = ['nombre', 'numero_resguardo', 'poblacion', 'texto']