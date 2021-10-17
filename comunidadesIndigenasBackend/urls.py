from django.contrib                 import admin
from django.urls                    import path
from comunidadesIndigenasApp        import views
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)


urlpatterns = [
    path('admin/',                                   admin.site.urls),
    path('login/',                                   TokenObtainPairView.as_view()), # use credentials to return tokens
    path('refresh/',                                 TokenRefreshView.as_view()), # generate new access token
    path('user/',                                    views.UserCreateView.as_view()), # create a new user
    path('user/<int:pk>/',                           views.UserDetailView.as_view()), # check info for an specific us
    path('asociacion/create/',                       views.AsociacionCreateView.as_view()), 
    path('asociacion/<int:user>/<int:pk>/',          views.AsociacionDetailView.as_view()), 
    path('asociacion/update/<int:user>/<int:pk>/',   views.AsociacionUpdateView.as_view()), 
    path('asociacion/remove/<int:user>/<int:pk>/',   views.AsociacionDeleteView.as_view()), 
    path('asociacion/<int:user>/<str:nombre>/',      views.AsociacionNombreView.as_view()),
    path('municipio/create/',                        views.MunicipioCreateView.as_view()),
    path('municipio/<int:user>/<int:pk>/',           views.MunicipioDetailView.as_view()), 
    path('municipio/update/<int:user>/<int:pk>/',    views.MunicipioUpdateView.as_view()), 
    path('municipio/remove/<int:user>/<int:pk>/',    views.MunicipioDeleteView.as_view()), 
    path('municipio/<int:user>/<str:nombre>/',       views.MunicipioNombreView.as_view()),
    path('departamento/create/',                     views.DepartamentoCreateView.as_view()),
    path('departamento/<int:pk>/',        views.DepartamentoDetailView.as_view()), 
    path('departamento/update/<int:user>/<int:pk>/', views.DepartamentoUpdateView.as_view()), 
    path('departamento/remove/<int:user>/<int:pk>/', views.DepartamentoDeleteView.as_view()), 
    path('departamento/<int:user>/<str:nombre>/',    views.DepartamentoNombreView.as_view()),
    path('resguardo/create/',                        views.ResguardoCreateView.as_view()),
    path('resguardo/<int:user>/<int:pk>/',           views.ResguardoDetailView.as_view()), 
    path('resguardo/update/<int:user>/<int:pk>/',    views.ResguardoUpdateView.as_view()), 
    path('resguardo/remove/<int:user>/<int:pk>/',    views.ResguardoDeleteView.as_view()), 
    path('resguardo/<int:user>/<str:nombre>/',       views.ResguardoNombreView.as_view()),
]
