from django.contrib import admin

from .models import *

# Register your models here.
@admin.register(Eje)
class EjeAdmin(admin.ModelAdmin):
    '''Admin View for Eje'''

    list_display = (
        "codigo",
        "nombre",
        "nombre",
        "estrategia",
        "problematica",
    )
    list_filter = list_display


@admin.register(Resultado)
class ResultadoAdmin(admin.ModelAdmin):

    list_display = (
        "codigo",
        "resultado",
        "presupuesto",
        "eje",
    )
    

@admin.register(Indicador)
class IndicadorAdmin(admin.ModelAdmin):
    '''Admin View for Indicador'''

    list_display = ("codigo",
        "alcance",
        "periodicidad",
        "fuente_informacion",
        "notas",
        "informacion_requerida",)
    

@admin.register(Institucion)
class InstitucionAdmin(admin.ModelAdmin):
    '''Admin View for Institucion'''

    list_display = ("nombre", "codigo",)
    

@admin.register(FuenteVerificacion)
class FuenteVerificacionAdmin(admin.ModelAdmin):
    '''Admin View for FuenteVerificacion'''

    list_display = ("nombre", "codigo",)


@admin.register(FactorDesagregacion)
class FactorDesagregacionAdmin(admin.ModelAdmin):
    '''Admin View for FactorDesagregacion'''

    list_display = ("nombre", "codigo",)


@admin.register(ValorFactor)
class ValorFactorAdmin(admin.ModelAdmin):
    '''Admin View for ValorFactor'''

    list_display = ("valor",
        "codigo",
        "categoria",)


@admin.register(Formula)
class FormulaAdmin(admin.ModelAdmin):
    '''Admin View for Formula'''

    list_display = ("nombre",
        "formula",
        "codigo",
        "indicador",)


@admin.register(Variable)
class VariableAdmin(admin.ModelAdmin):
    '''Admin View for Variable'''

    list_display = (
        "nombre",
        "tipo",
        "formula",
    )


@admin.register(MedicionIndicador)
class MedicionIndicadorAdmin(admin.ModelAdmin):
    '''Admin View for MedicionIndicador'''

    list_display = (
        "codigo",
        "contenido",
        "indicador",
        #"valores_factor",
        "area",
    )


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    '''Admin View for Area'''

    list_display = (
        "nombre",
        "descripcion",
        "municipio",
    )


@admin.register(Municipio)
class MunicipioAdmin(admin.ModelAdmin):
    '''Admin View for Municipio'''

    list_display = (
        "nombre",
        "codigo",
        "departamento",
    )
    
    
@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    '''Admin View for Departamento'''

    list_display = (
        "nombre",
        "codigo",
    )


@admin.register(ValorVariable)
class ValorVariableAdmin(admin.ModelAdmin):
    '''Admin View for ValorVariable'''

    list_display = (
        "variable",
        "medicion",
        "valor",
    )