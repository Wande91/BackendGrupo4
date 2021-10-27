from django.utils.translation import override
from comunidadesIndigenasApp.models.municipio    import Municipio
from comunidadesIndigenasApp.models.departamento import Departamento
from rest_framework                              import serializers

from comunidadesIndigenasApp.serializers.departamentoSerializer import DepartamentoSerializer

class MunicipioSerializer(serializers.ModelSerializer):
    #departamento = DepartamentoSerializer()
    class Meta:
        model  = Municipio
        fields =['nombre', 'texto', 'departamento']

    def to_representation(self, obj):
        municipio    = Municipio.objects.get(id =obj.id)
        departamento = Departamento.objects.get(id = obj.departamento.id)
        return {
            'id'     : municipio.id,
            'nombre' : municipio.nombre,
            'texto'  : municipio.texto,
            'departamento' : {
                'id'       : departamento.id,
                'nombre'   : departamento.nombre,
            }
        }