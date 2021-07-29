#Librerias de 3ros
from rest_framework import serializers

#librerias propias
from .models import * 

#Serializadores de modelos para rest api
class MedicionIndicadorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MedicionIndicador
        fields = [
            'codigo',
            'contenido',
            'indicador',
            'valores_factor',
            'area',
        ]


class EjeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Eje
        fields = [
            "codigo",
            "nombre",
            "estrategia",
            "problematica",
        ]


class ResultadoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Resultado
        fields = [
            "codigo",
            "resultado",
            "presupuesto",
            "eje",
        ]


class IndicadorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Indicador
        fields = [
            "codigo",
            "alcance",
            "periodicidad",
            "fuente_informacion",
            "notas",
            "informacion_requerida",
            "factores_desagregacion",
            "fuentes_verificacion",
            "instituciones",
            "resultado",
        ]


class InstitucionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Institucion
        fields = [
            "nombre",
            "codigo",
        ]


class FuenteVerificacionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FuenteVerificacion
        fields = [
            "nombre",
            "codigo",
        ]


class FactorDesagregacionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FactorDesagregacion
        fields = [
            "nombre",
            "codigo",
        ]


class ValorFactorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ValorFactor
        fields = [
            "valor",
            "codigo",
            "categoria",
        ]


class FormulaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Formula
        fields = [
            "nombre",
            "formula",
            "codigo",
            "indicador",
        ]


class VariableSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Variable
        fields = [
            "nombre",
            "tipo",
            "formula",
        ]


class UnidadMedidaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UnidadMedida
        fields = [
            "nombre",
            "simbolo",
            "variable",
        ]


class AreaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Area
        fields = [
            "nombre",
            "descripcion",
            "municipio",
        ]


class MunicipioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Municipio
        fields = [
            "nombre",
            "codigo",
            "departamento",
        ]


class DepartamentoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Departamento
        fields = [
            "nombre",
            "codigo",
        ]


class ValorVariableSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ValorVariable
        fields = [
            "variable",
            "medicion",
            "valor",
        ]