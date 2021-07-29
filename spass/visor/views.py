#librerias de django
from django.shortcuts import render

#librerias de 3ros
from rest_framework import viewsets, permissions

#librerias propias
from .models import *
from .serializers import *

#Views API
class MedicionViewSet(viewsets.ModelViewSet):
    queryset = MedicionIndicador.objects.all()
    serializer_class = MedicionIndicadorSerializer
    permission_classes = [permissions.AllowAny]


class EjeViewSet(viewsets.ModelViewSet):
    queryset = Eje.objects.all()
    serializer_class = EjeSerializer
    permission_classes = [permissions.AllowAny]



class MedicionIndicadorViewSet(viewsets.ModelViewSet):
    queryset = MedicionIndicador.objects.all()
    serializer_class = MedicionIndicadorSerializer
    permission_classes = [permissions.AllowAny]



class ResultadoViewSet(viewsets.ModelViewSet):
    queryset = Resultado.objects.all()
    serializer_class = ResultadoSerializer
    permission_classes = [permissions.AllowAny]



class IndicadorViewSet(viewsets.ModelViewSet):
    queryset = Indicador.objects.all()
    serializer_class = IndicadorSerializer
    permission_classes = [permissions.AllowAny]



class InstitucionViewSet(viewsets.ModelViewSet):
    queryset = Institucion.objects.all()
    serializer_class = InstitucionSerializer
    permission_classes = [permissions.AllowAny]



class FuenteVerificacionViewSet(viewsets.ModelViewSet):
    queryset = FuenteVerificacion.objects.all()
    serializer_class = FuenteVerificacionSerializer
    permission_classes = [permissions.AllowAny]



class FactorDesagregacionViewSet(viewsets.ModelViewSet):
    queryset = FactorDesagregacion.objects.all()
    serializer_class = FactorDesagregacionSerializer
    permission_classes = [permissions.AllowAny]



class ValorFactorViewSet(viewsets.ModelViewSet):
    queryset = ValorFactor.objects.all()
    serializer_class = ValorFactorSerializer
    permission_classes = [permissions.AllowAny]



class FormulaViewSet(viewsets.ModelViewSet):
    queryset = Formula.objects.all()
    serializer_class = FormulaSerializer
    permission_classes = [permissions.AllowAny]



class VariableViewSet(viewsets.ModelViewSet):
    queryset = Variable.objects.all()
    serializer_class = VariableSerializer
    permission_classes = [permissions.AllowAny]



class UnidadMedidaViewSet(viewsets.ModelViewSet):
    queryset = UnidadMedida.objects.all()
    serializer_class = UnidadMedidaSerializer
    permission_classes = [permissions.AllowAny]


class AreaViewSet(viewsets.ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer
    permission_classes = [permissions.AllowAny]


class MunicipioViewSet(viewsets.ModelViewSet):
    queryset = Municipio.objects.all()
    serializer_class = MunicipioSerializer
    permission_classes = [permissions.AllowAny]


class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
    permission_classes = [permissions.AllowAny]


class ValorVariableViewSet(viewsets.ModelViewSet):
    queryset = ValorVariable.objects.all()
    serializer_class = ValorVariableSerializer
    permission_classes = [permissions.AllowAny]
