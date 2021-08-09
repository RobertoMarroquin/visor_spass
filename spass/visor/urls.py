#librerias de Django
from django.urls import include, path
#librerias de 3ros
from rest_framework import routers
#librerias propias
from .views import *

router = routers.DefaultRouter()
router.register(r'indicador', IndicadorViewSet)
router.register(r'mediciones', MedicionViewSet)
router.register(r'eje', EjeViewSet)
router.register(r'variable', VariableViewSet)
router.register(r'resultado', ResultadoViewSet)
router.register(r'institucion', InstitucionViewSet)
router.register(r'fuenteVerificacion', FuenteVerificacionViewSet)
router.register(r'factorDesagregacion', FactorDesagregacionViewSet)
router.register(r'valorFactor', ValorFactorViewSet)
router.register(r'formula', FormulaViewSet)
router.register(r'unidadMedida', UnidadMedidaViewSet)
router.register(r'area', AreaViewSet)
router.register(r'municipio', MunicipioViewSet)
router.register(r'departamento', DepartamentoViewSet)
router.register(r'valorVariable', ValorVariableViewSet)




app_name = 'visor'
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('indicador-detail/<int:pk>/', IndicadorDetail.as_view(), name ='indicador-detail'),
    path('mediciones-detail/<int:pk>/', MedicionDetail.as_view(), name ='mediciones-detail'),
    path('eje-detail/<int:pk>/', EjeDetail.as_view(), name ='eje-detail'),
    path('resultado-detail/<int:pk>/', ResultadoDetail.as_view(), name ='resultado-detail'),
    path('institucion-detail/<int:pk>/', InstitucionDetail.as_view(), name ='institucion-detail'),
    path('fuenteVerificacion-detail/<int:pk>/', FuenteVerificacionDetail.as_view(), name ='fuenteVerificacion-detail'),
    path('factorDesagregacion-detail/<int:pk>/', FactorDesagregacionDetail.as_view(), name ='factorDesagregacion-detail'),
    path('valorFactor-detail/<int:pk>/', ValorFactorDetail.as_view(), name ='valorFactor-detail'),
    path('formula-detail/<int:pk>/', FormulaDetail.as_view(), name ='formula-detail'),
    path('unidadMedida-detail/<int:pk>/', UnidadMedidaDetail.as_view(), name ='unidadMedida-detail'),
    path('area-detail/<int:pk>/', AreaDetail.as_view(), name ='area-detail'),
    path('municipio-detail/<int:pk>/', MunicipioDetail.as_view(), name ='municipio-detail'),
    path('departamento-detail/<int:pk>/', DepartamentoDetail.as_view(), name ='departamento-detail'),
    path('valorVariable-detail/<int:pk>/', ValorVariableDetail.as_view(), name ='valorVariable-detail'),
]