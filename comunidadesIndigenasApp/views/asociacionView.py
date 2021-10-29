from django.conf                                              import settings
from rest_framework                                           import generics, status
from rest_framework.response                                  import Response
from rest_framework.permissions                               import IsAuthenticated
from rest_framework_simplejwt.backends                        import TokenBackend
from comunidadesIndigenasApp.models.asociacion                import Asociacion
from comunidadesIndigenasApp.serializers.asociacionSerializer import AsociacionSerializer

class AsociacionDetailView(generics.RetrieveAPIView):
  serializer_class   = AsociacionSerializer
  permission_classes = (IsAuthenticated,)
  queryset           = Asociacion.objects.all()
  
  def get(self, request, *args, **kwargs):
      token        = request.META.get('HTTP_AUTHORIZATION')[7:]
      tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
      valid_data   = tokenBackend.decode(token,verify=False)
      
      if valid_data['user_id'] != kwargs['user']:
          stringResponse = {'detail':'Unauthorized Request'}
          return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
      
      return super().get(request, *args, **kwargs)

class AsociacionMun(generics.ListAPIView):
  serializer_class   = AsociacionSerializer
  permission_classes = (IsAuthenticated,)
  
  def get_queryset(self):
      token        = self.request.META.get('HTTP_AUTHORIZATION')[7:]
      tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
      valid_data   = tokenBackend.decode(token,verify=False)
      
      if valid_data['user_id'] != self.kwargs['user']:
          return 
          
      queryset = Asociacion.objects.filter(municipio=self.kwargs['municipio'])
      return queryset
  
class AsociacionList(generics.ListAPIView):
  serializer_class = AsociacionSerializer
  permission_classes = (IsAuthenticated,)
  queryset = Asociacion.objects.all()

  def get(self, request, *args, **kwargs):
      token        = self.request.META.get('HTTP_AUTHORIZATION')[7:]
      tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
      valid_data   = tokenBackend.decode(token,verify=False)
      
      if valid_data['user_id'] != self.kwargs['user']:
          stringResponse = {'detail':'Unauthorized Request'}
          return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

      return super().get(request, *args, **kwargs)

class AsociacionCreateView(generics.CreateAPIView):
  serializer_class   = AsociacionSerializer
  permission_classes = (IsAuthenticated,)
  
  def post(self, request, *args, **kwargs):
      token        = request.META.get('HTTP_AUTHORIZATION')[7:]
      tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
      valid_data   = tokenBackend.decode(token,verify=False)
        
      if valid_data['user_id'] != kwargs['user']:
        stringResponse = {'detail':'Unauthorized Request'}
        return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        
      serializer = AsociacionSerializer(data=request.data)
      serializer.is_valid(raise_exception=True)
      serializer.save()
    
      return Response("Inserción exitosa", status=status.HTTP_201_CREATED)
  
class AsociacionUpdateView(generics.UpdateAPIView):
  serializer_class   = AsociacionSerializer
  permission_classes = (IsAuthenticated,)
  queryset           = Asociacion.objects.all()
  
  def update(self, request, *args, **kwargs):
      token        = request.META.get('HTTP_AUTHORIZATION')[7:]
      tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
      valid_data   = tokenBackend.decode(token,verify=False)
        
      if valid_data['user_id'] != kwargs['user']:
          stringResponse = {'detail':'Unauthorized Request'}
          return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        
      return super().update(request, *args, **kwargs)
    
class AsociacionDeleteView(generics.DestroyAPIView):
  serializer_class   = AsociacionSerializer
  permission_classes = (IsAuthenticated,)
  queryset           = Asociacion.objects.all()
  
  def delete(self, request, *args, **kwargs):
      token        = request.META.get('HTTP_AUTHORIZATION')[7:]
      tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
      valid_data   = tokenBackend.decode(token,verify=False)
        
      if valid_data['user_id'] != kwargs['user']:
          stringResponse = {'detail':'Unauthorized Request'}
          return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

      return super().destroy(request, *args, **kwargs)