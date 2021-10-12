from django.conf                                          import settings
from rest_framework                                       import generics, status
from rest_framework.response                              import Response
from rest_framework.permissions                           import IsAuthenticated
from rest_framework_simplejwt.backends                    import TokenBackend

from comunidadesIndigenasApp.models.resguardo               import Resguardo
from comunidadesIndigenasApp.serializers.resguardoSerializer import ResguardoSerializer


class ResguardoDetailView(generics.RetrieveAPIView):
    serializer_class   = ResguardoSerializer
    permission_classes = (IsAuthenticated, )
    queryset           = Resguardo.objects.all()

    def get(self, request, *args, **kwargs):
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
          
        if valid_data['user_id'] != kwargs['user']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        return super().get(request, *args, **kwargs)

# Filtrar resguardos a partir de municipios

class ResguardoNombreView(generics.ListAPIView):
    serializer_class   = ResguardoSerializer
    permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):
        token        = self.request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        if valid_data['user_id'] != self.kwargs['user']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        queryset = Resguardo.objects.filter(nombre=self.kwargs['nombre'])
        return queryset


class ResguardoCreateView(generics.CreateAPIView):
    serializer_class   = ResguardoSerializer
    permission_classes = (IsAuthenticated, )
    
    def post(self, request, *args, **kwargs):
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        if valid_data['user_id'] != request.data['user_id']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        
        serializer = ResguardoSerializer(data=request.data['Resguardo_data'])
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response("Insercion exitosa", status=status.HTTP_201_CREATED)


class ResguardoUpdateView(generics.UpdateAPIView):
    serializer_class   = ResguardoSerializer
    permission_classes = (IsAuthenticated, )
    queryset           = Resguardo.objects.all()

    def update(self, request, *args, **kwargs):
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        if valid_data['user_id'] != kwargs['user']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        return super().update(request, *args, **kwargs)


class ResguardoDeleteView(generics.DestroyAPIView):
    serializer_class   = ResguardoSerializer
    permission_classes = (IsAuthenticated, )
    queryset           = Resguardo.objects.all()

    def delete(self, request, *args, **kwargs):
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        if valid_data['user_id'] != kwargs['user']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        return super().destroy(request, *args, **kwargs)