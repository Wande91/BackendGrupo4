from django.contrib                 import admin
from django.urls                    import path
from rest_framework import serializers
from comunidadesIndigenasApp        import views
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)


urlpatterns = [
    path('admin/',                                      admin.site.urls),
    path('login/',                                      TokenObtainPairView.as_view()), # use credentials to return tokens
    path('refresh/',                                    TokenRefreshView.as_view()), # generate new access token
    path('user/',                                       views.UserCreateView.as_view()), # create a new user
    path('user/<int:pk>/',                              views.UserDetailView.as_view()), # check info for an specific us

    #Informacion Department por id
    path('departamento/<int:user>/<int:pk>/',           views.DepartamentoDetailView.as_view()), 
    #Informacion Departamento por nombre
    path('departamento/<int:user>/<str:nombre>/',       views.DepartamentoNombreView.as_view()),
    #Informacion todos los Departamentos
    path('departamento/list/<int:user>/',               views.DepartamentoList.as_view()),
    
    path('departamento/create/<int:user>/',             views.DepartamentoCreateView.as_view()),
    path('departamento/update/<int:user>/<int:pk>/',    views.DepartamentoUpdateView.as_view()), 
    path('departamento/remove/<int:user>/<int:pk>/',    views.DepartamentoDeleteView.as_view()), 
    
    #Informacion Municipio por id
    path('municipio/<int:user>/<int:pk>/',               views.MunicipioDetailView.as_view()), 
    #Informacion Municipio por Departamento
    path('municipio/filter/<int:user>/<int:departamento>/',    views.MunicipioDepView.as_view()),
    #Informacion Municipio General
    path('municipio/<int:user>/list/',                  views.MunicipioList.as_view()),
    
    path('municipio/create/<int:user>/',                views.MunicipioCreateView.as_view()),
    path('municipio/update/<int:user>/<int:pk>/',       views.MunicipioUpdateView.as_view()), 
    path('municipio/remove/<int:user>/<int:pk>/',       views.MunicipioDeleteView.as_view()), 
    
    #Informacion Asociacion por id
    path('asociacion/<int:user>/<int:pk>/',             views.AsociacionDetailView.as_view()), 
    #Informacion Asociacion por municipio
    path('asociacion/filter/<int:user>/<int:municipio>/',      views.AsociacionMun.as_view()),
    #Informacion Asociacion general
    path('asociacion/<int:user>/list/',                 views.AsociacionList.as_view()),
    
    path('asociacion/create/<int:user>/',               views.AsociacionCreateView.as_view()), 
    path('asociacion/update/<int:user>/<int:pk>/',      views.AsociacionUpdateView.as_view()), 
    path('asociacion/remove/<int:user>/<int:pk>/',      views.AsociacionDeleteView.as_view()), 

    #Informacion Resguardo por id
    path('resguardo/<int:user>/<int:pk>/',              views.ResguardoDetailView.as_view()), 
    #Informacion Resguardo por Asociacion
    path('resguardo/filter/<int:user>/<int:asociacion>/',      views.ResguardoAsoc.as_view()),
    #Informacion Resguardo general (falta ajustar)
    path('resguardo/<int:user>/list/',                  views.ResguardoList.as_view()),

    path('resguardo/create/<int:user>/',                views.ResguardoCreateView.as_view()),
    path('resguardo/update/<int:user>/<int:pk>/',       views.ResguardoUpdateView.as_view()), 
    path('resguardo/remove/<int:user>/<int:pk>/',       views.ResguardoDeleteView.as_view()),   
]
