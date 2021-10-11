from comunidadesIndigenasApp.models.asociacion import Asociacion
from rest_framework                            import serializers

class AsociacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asociacion
        fields = ['nombre','texto']