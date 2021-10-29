from django.conf                                        import settings
from rest_framework                                     import status, views, generics
from rest_framework.response                            import Response
from rest_framework_simplejwt.serializers               import TokenObtainPairSerializer
from rest_framework.permissions                         import IsAuthenticated
from comunidadesIndigenasApp.serializers.userSerializer import UserSerializer
from rest_framework_simplejwt.backends                  import TokenBackend

from comunidadesIndigenasApp.models.user                import User
from comunidadesIndigenasApp.serializers.userSerializer import UserSerializer

class UserCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        tokenData = {'username':request.data['username'],
                    'password':request.data['password']}
        try:
            tokenSerializer = TokenObtainPairSerializer(data=tokenData)
            tokenSerializer.is_valid(raise_exception=True)
            return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response('Error in token generation', status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
class UserUpdateView(generics.UpdateAPIView):
    serializer_class   = UserSerializer
    permission_classes = (IsAuthenticated, )
    queryset           = User.objects.all()

    def update(self, request, *args, **kwargs):
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        if valid_data['user_id'] != kwargs['user']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        return super().update(request, *args, **kwargs)


class UserDeleteView(generics.DestroyAPIView):
    serializer_class   = UserSerializer
    permission_classes = (IsAuthenticated, )
    queryset           = User.objects.all()

    def delete(self, request, *args, **kwargs):
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        if valid_data['user_id'] != kwargs['user']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        return super().destroy(request, *args, **kwargs)