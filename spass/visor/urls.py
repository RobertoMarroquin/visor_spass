#librerias de Django
from django.urls import include, path
#librerias de 3ros
from rest_framework import routers
#librerias propias
from .views import *

router = routers.DefaultRouter()
router.register(r'mediciones', MedicionViewSet)
router.register(r'eje', EjeViewSet)
router.register(r'resultado', ResultadoViewSet)
router.register(r'indicador', IndicadorViewSet)
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
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]