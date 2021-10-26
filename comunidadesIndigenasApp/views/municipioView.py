from django.conf                                              import settings
from rest_framework                                           import generics, status
from rest_framework.response                                  import Response
from rest_framework.permissions                               import IsAuthenticated
from rest_framework_simplejwt.backends                        import TokenBackend
from comunidadesIndigenasApp.models.municipio                 import Municipio
from comunidadesIndigenasApp.serializers.municipioSerializer  import MunicipioSerializer



class MunicipioDetailView(generics.RetrieveAPIView):
  queryset           = Municipio.objects.all()
  serializer_class   = MunicipioSerializer
  
  def get(self, request, *args, **kwargs):  
      return super().get(request, *args, **kwargs)

class MunicipioDepView(generics.ListAPIView):
  serializer_class   = MunicipioSerializer
  
  def get_queryset(self):
      queryset = Municipio.objects.filter(departamento=self.kwargs['departamento'])
      return queryset

class MunicipioList(generics.ListAPIView):
  serializer_class   = MunicipioSerializer
  
  def get_queryset(self):
      queryset = Municipio.objects.all()
      return queryset
  
class MunicipioCreateView(generics.CreateAPIView):
  serializer_class   = MunicipioSerializer
  permission_classes = (IsAuthenticated,)
  
  def post(self, request, *args, **kwargs):
    
      token        = request.META.get('HTTP_AUTHORIZATION')[7:]
      tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
      valid_data   = tokenBackend.decode(token,verify=False)
        
      if valid_data['user_id'] != kwargs['user']:
        stringResponse = {'detail':'Unauthorized Request'}
        return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        
      serializer = MunicipioSerializer(data=request.data)
      serializer.is_valid(raise_exception=True)
      serializer.save()
      return Response("Inserción exitosa", status=status.HTTP_201_CREATED)
  
class MunicipioUpdateView(generics.UpdateAPIView):
  serializer_class   = MunicipioSerializer
  permission_classes = (IsAuthenticated,)
  queryset           = Municipio.objects.all()
  
  def update(self, request, *args, **kwargs):
      token        = request.META.get('HTTP_AUTHORIZATION')[7:]
      tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
      valid_data   = tokenBackend.decode(token,verify=False)
        
      if valid_data['user_id'] != kwargs['user']:
        stringResponse = {'detail':'Unauthorized Request'}
        return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

      return super().update(request, *args, **kwargs)
    
class MunicipioDeleteView(generics.DestroyAPIView):
  serializer_class   = MunicipioSerializer
  permission_classes = (IsAuthenticated,)
  queryset           = Municipio.objects.all()
  
  def delete(self, request, *args, **kwargs):
      token        = request.META.get('HTTP_AUTHORIZATION')[7:]
      tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
      valid_data   = tokenBackend.decode(token,verify=False)
        
      if valid_data['user_id'] != kwargs['user']:
        stringResponse = {'detail':'Unauthorized Request'}
        return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

      return super().destroy(request, *args, **kwargs)