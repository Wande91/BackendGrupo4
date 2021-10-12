from django.contrib                 import admin
from django.urls                    import path
from comunidadesIndigenasApp        import views as comIndigenasAppViews
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)


urlpatterns = [
    path('admin/',                                   admin.site.urls),
    path('login/',                                   TokenObtainPairView.as_view()), # use credentials to return tokens
    path('refresh/',                                 TokenRefreshView.as_view()), # generate new access token
    path('user/',                                    comIndigenasAppViews.UserCreateView.as_view()), # create a new user
    path('user/<int:pk>/',                           comIndigenasAppViews.UserDetailView.as_view()), # check info for an specific us
    path('asociacion/create/',                       comIndigenasAppViews.AsociacionCreateView.as_view()), 
    path('asociacion/<int:user>/<int:pk>/',          comIndigenasAppViews.AsociacionDetailView.as_view()), 
    path('asociacion/update/<int:user>/<int:pk>/',   comIndigenasAppViews.AsociacionUpdateView.as_view()), 
    path('asociacion/remove/<int:user>/<int:pk>/',   comIndigenasAppViews.AsociacionDeleteView.as_view()), 
    path('asociacion/<int:user>/<str:nombre>/',      comIndigenasAppViews.AsociacionNombreView.as_view()),
    path('municipio/create/',                        comIndigenasAppViews.MunicipioCreateView.as_view()),
    path('municipio/<int:user>/<int:pk>/',           comIndigenasAppViews.MunicipioDetailView.as_view()), 
    path('municipio/update/<int:user>/<int:pk>/',    comIndigenasAppViews.MunicipioUpdateView.as_view()), 
    path('municipio/remove/<int:user>/<int:pk>/',    comIndigenasAppViews.MunicipioDeleteView.as_view()), 
    path('municipio/<int:user>/<str:nombre>/',       comIndigenasAppViews.MunicipioNombreView.as_view()),
    path('departamento/create/',                     comIndigenasAppViews.DepartamentoCreateView.as_view()),
    path('departamento/<int:user>/<int:pk>/',        comIndigenasAppViews.DepartamentoDetailView.as_view()), 
    path('departamento/update/<int:user>/<int:pk>/', comIndigenasAppViews.DepartamentoUpdateView.as_view()), 
    path('departamento/remove/<int:user>/<int:pk>/', comIndigenasAppViews.DepartamentoDeleteView.as_view()), 
    path('departamento/<int:user>/<str:nombre>/',    comIndigenasAppViews.DepartamentoNombreView.as_view()),
    path('resguardo/create/',                        comIndigenasAppViews.ResguardoCreateView.as_view()),
    path('resguardo/<int:user>/<int:pk>/',           comIndigenasAppViews.ResguardoDetailView.as_view()), 
    path('resguardo/update/<int:user>/<int:pk>/',    comIndigenasAppViews.ResguardoUpdateView.as_view()), 
    path('resguardo/remove/<int:user>/<int:pk>/',    comIndigenasAppViews.ResguardoDeleteView.as_view()), 
    path('resguardo/<int:user>/<str:nombre>/',       comIndigenasAppViews.ResguardoNombreView.as_view()),
]
