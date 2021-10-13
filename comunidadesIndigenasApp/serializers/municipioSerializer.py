from comunidadesIndigenasApp.models.municipio    import Municipio
from comunidadesIndigenasApp.models.departamento import Departamento
from rest_framework                              import serializers

class MunicipioSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Municipio
        fields =['nombre', 'texto']

        def to_representation(self, obj):
            departamento = Departamento.objects.get(id = obj.id)
            municipio    = Municipio.objects.get(id =obj.id)
            return {
                'id'              : municipio.id,
                'nombre'          : municipio.nombre,
                'texto'           : municipio.texto,
                'departamento_id' : {
                    'id'     : departamento.id,
                    'nombre' : departamento.nombre
                }
            }