#Librerias de 3ros
from rest_framework import serializers

#librerias propias
from .models import * 

#Serializadores de modelos para rest api
class MedicionIndicadorSerializer(serializers.HyperlinkedModelSerializer):
    indicador = serializers.PrimaryKeyRelatedField(read_only=True)
    area = serializers.PrimaryKeyRelatedField(read_only=True)
    valores_factor = serializers.StringRelatedField(read_only=True,many=True)
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
    #eje = serializers.StringRelatedField()
    eje = serializers.SlugRelatedField(read_only=True, slug_field='id')
   
    class Meta:
        model = Resultado
        fields = [
            "codigo",
            "resultado",
            "presupuesto",
            "eje",
        ]


class IndicadorSerializer(serializers.HyperlinkedModelSerializer):
    factores_desagregacion = serializers.StringRelatedField(many=True)
    #fuentes_verificacion  = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    fuentes_verificacion  = serializers.StringRelatedField(many=True)
    instituciones  = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    resultado  = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Indicador
        fields = [
            "nombre",
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
        read_only_fields = [
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
    categoria = serializers.PrimaryKeyRelatedField(read_only=True)
    categoria_nombre = serializers.SlugRelatedField(source='categoria',slug_field='nombre',read_only=True,)

    class Meta:
        model = ValorFactor
        fields = [
            "valor",
            "codigo",
            "categoria",
            "categoria_nombre"
        ]


class FormulaSerializer(serializers.HyperlinkedModelSerializer):
    indicador =  serializers.PrimaryKeyRelatedField(read_only=True)
    indicador_nombre = serializers.SlugRelatedField(source='indicador',slug_field='nombre',read_only=True)
    class Meta:
        model = Formula
        fields = [
            "nombre",
            "formula",
            "codigo",
            "indicador",
            'indicador_nombre',
        ]


class VariableSerializer(serializers.HyperlinkedModelSerializer):
    formula = serializers.PrimaryKeyRelatedField(read_only=True)
    formula_formula = serializers.SlugRelatedField(source='formula',slug_field='formula',read_only=True)
    class Meta:
        model = Variable
        fields = [
            "nombre",
            "tipo",
            "formula",'formula_formula'
        ]


class UnidadMedidaSerializer(serializers.HyperlinkedModelSerializer):
    variable = serializers.PrimaryKeyRelatedField(read_only=True)
    variable_nombre = serializers.SlugRelatedField(source='variable',slug_field='nombre',read_only=True)
    class Meta:
        model = UnidadMedida
        fields = [
            "nombre",
            "simbolo",
            "variable",
            'variable_nombre'
        ]


class AreaSerializer(serializers.HyperlinkedModelSerializer):
    municipio = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Area
        fields = [
            "nombre",
            "descripcion",
            "municipio",
        ]


class MunicipioSerializer(serializers.HyperlinkedModelSerializer):
    departamento = serializers.PrimaryKeyRelatedField(read_only=True)
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
    variable = serializers.PrimaryKeyRelatedField(read_only=True)
    medicion = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = ValorVariable
        fields = [
            "variable",
            "medicion",
            "valor",
        ]