from django.conf                                          import settings
from django.db.models.query                               import QuerySet
from rest_framework                                       import generics, status
from rest_framework.response                              import Response
from rest_framework.permissions                           import IsAuthenticated
from rest_framework_simplejwt.backends                    import TokenBackend
from BackEnd.BackendGrupo4.comunidadesIndigenasApp        import serializers
from BackEnd.BackendGrupo4.comunidadesIndigenasApp.models import municipio

from comunidadesIndigenasApp.models.resguardo               import Resguardo
from comunidadesIndigenasApp.serializers.reguardoSerializer import ResguardoSerializer


class ResguardoDetailView(generics.RetrieveAPIView):
    serializer_class   = ResguardoSerializer
    permission_classes = (IsAuthenticated, )
    queryset           = Resguardo.objects.all()

    def get(self, request, *args, **kwargs):
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token, verify=False)

        return super().update(request, *args, **kwargs)

# Filtrar resguardos a partir de municipios

class ResguardoMunicipioView(generics.DestroyAPIView):
    serializer_class   = ResguardoSerializer
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        queryset = Resguardo.objects.filter(municipio_id=self.kwargs['municipio'])
        return queryset


class ResguardoCreateView(generics.CreateAPIView):
    serializer_class   = ResguardoSerializer
    permission_classes = (IsAuthenticated, )
    def post(self, request, *args, **kwargs):
        serializer = ResguardoSerializer(data=request.data['resguardo_data'])
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response("Transacción exitosa", status=status.HTTP_201_CREATED)


class ResguardoUpdateView(generics.UpdateAPIView):
    serializer_class   = ResguardoSerializer
    permission_classes = (IsAuthenticated, )
    queryset           = Resguardo.objects.all()

    def put(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)


class ResguardoDeleteView(generics.DestroyAPIView):
    serializer_class   = ResguardoSerializer
    permission_classes = (IsAuthenticated, )
    queryset           = Resguardo.objects.all()

    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)