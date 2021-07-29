from django.db import models

# Modelos de visualizador de datos
class Eje(models.Model):
    codigo = models.CharField("Codigo", max_length=50,blank=True, null=True)
    nombre = models.CharField("Nombre",max_length=150,blank=True, null=True)
    estrategia = models.TextField("Estrategia")
    problematica = models.TextField("Problematica")

    class Meta:
        verbose_name = ("Eje")
        verbose_name_plural = ("Ejes")

    def __str__(self):
        return self.codigo


class Resultado(models.Model):
    codigo = models.CharField(("Codigo"), max_length=50)
    resultado = models.TextField("Resultado")
    presupuesto = models.TextField("Presupuesto")
    eje = models.ForeignKey("visor.Eje", on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = ("Resultado")
        verbose_name_plural = ("Resultados")

    def __str__(self):
        return self.codigo


class Indicador(models.Model):
    codigo = models.CharField('Codigo', max_length=50, blank=True, null=True)
    alcance = models.IntegerField(("Alcance"), choices=((1,"Corto"),(2,"Medio"),(3,"Largo")), blank=True, null=True)
    periodicidad = models.IntegerField(("Periodicidad de medicion"), choices=((1,"Anual"),(2,"Semestral"),(3,'Cuatrimestral'),(4,"Trimestral"),(5,'Mensual')), blank=True, null=True)
    fuente_informacion = models.TextField(("Fuente de Informacion"))
    notas = models.TextField(("Notas Tecnicas"))
    informacion_requerida = models.TextField(("Informacion a Requerir"))
    
    factores_desagregacion = models.ManyToManyField('visor.FactorDesagregacion', related_name='indicador')
    fuentes_verificacion = models.ManyToManyField('visor.FuenteVerificacion', related_name='indicador')
    instituciones = models.ManyToManyField('visor.Institucion', related_name='indicador')
    resultado = models.ForeignKey("visor.Resultado", on_delete=models.CASCADE,related_name='indicadores')
    
    class Meta:
        verbose_name = ("Indicador")
        verbose_name_plural = ("Indicadores")

    def __str__(self):
        return self.codigo


class Institucion(models.Model):
    nombre = models.CharField('Nombre', max_length=150, blank=True, null=True)
    codigo = models.CharField(("Codigo"), max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = 'Institucion'
        verbose_name_plural = 'Instituciones'

    def __str__(self):
        return f'{self.codigo}' 


class FuenteVerificacion(models.Model):
    nombre = models.CharField('Nombre', max_length=150, blank=True, null=True)
    codigo = models.CharField(("Codigo"), max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = 'Fuente Verificacion'
        verbose_name_plural = 'Fuentes Verificacion'

    def __str__(self):
        return f'{self.codigo}' 


class FactorDesagregacion(models.Model):
    nombre = models.CharField('Nombre', max_length=150, blank=True, null=True)
    codigo = models.CharField(("Codigo"), max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = 'Factor Desagregacion'
        verbose_name_plural = 'Factores Desagregacion'

    def __str__(self):
        return f'{self.codigo}' 


class ValorFactor(models.Model):
    valor = models.CharField(("Valor"), max_length=150)
    codigo = models.CharField(("Codigo"), max_length=50)
    categoria = models.ForeignKey("visor.FactorDesagregacion", on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Valor Factor'
        verbose_name_plural = 'Valores Factor'

    def __str__(self):


        return f'{self.valor}' 


class Formula(models.Model):
    nombre = models.CharField('Nombre', max_length=150, blank=True, null=True)
    formula = models.TextField(("Formula"))
    codigo = models.CharField(("Codigo"), max_length=50)
    indicador = models.ForeignKey('visor.Indicador', related_name='indicador', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Formula'
        verbose_name_plural = 'Formulas'

    def __str__(self):
        return f'{self.codigo}'




class Variable(models.Model):
    nombre = models.CharField('Nombre', max_length=150, blank=True, null=True)
    tipo = models.IntegerField(("Tipo"), choices=((1,"Cualitativo"),(2,"Cuantitativo")), default=1)
    formula = models.ForeignKey("visor.Formula", on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Variable'
        verbose_name_plural = 'Variables'

    def __str__(self):
        """Unicode representation of Variable."""
        return f'{self.nombre}'


class UnidadMedida(models.Model):
    nombre = models.CharField('Nombre', max_length=150, blank=True, null=True)
    simbolo = models.CharField(("Simbolo"), max_length=5)
    variable = models.ForeignKey('visor.Variable', on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Unidad edida'
        verbose_name_plural = 'Unidades Medida'

    def __str__(self):
        return f'{self.nombre}'


class MedicionIndicador(models.Model):
    codigo = models.CharField('Codigo', max_length=50)
    contenido = models.TextField(("Contenido"))
    indicador = models.ForeignKey("visor.Indicador", on_delete=models.CASCADE, related_name="mediciones")
    valores_factor = models.ManyToManyField("visor.ValorFactor")
    area = models.ForeignKey('visor.Area', related_name='indicadores', on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Medicion de Indicador'
 
    def __str__(self):
        return f'{self.codigo}' 


class Area(models.Model):
    nombre = models.CharField('Nombre', max_length=150, blank=True, null=True)
    descripcion = models.TextField("Descripcion")
    municipio = models.ForeignKey('visor.municipio', related_name='areas', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Area'
        verbose_name_plural = 'Areas'

    def __str__(self):
        return f'{self.nombre }'


class Municipio(models.Model):
    nombre = models.CharField('Nombre', max_length=150, blank=True, null=True)
    codigo = models.CharField('Codigo', max_length=50)
    departamento = models.ForeignKey('visor.Departamento', related_name='municipios', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Municipio'
        verbose_name_plural = 'Municipios'

    def __str__(self):
        return f'{self.nombre}'


class Departamento(models.Model):
    nombre = models.CharField('Nombre', max_length=150, blank=True, null=True)
    codigo = models.CharField(("Codigo"), max_length=50)

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'

    def __str__(self):
        return f'{self.nombre}'


class ValorVariable(models.Model):
    variable = models.ForeignKey('visor.Variable', related_name='valor', on_delete=models.CASCADE)
    medicion = models.ForeignKey('visor.MedicionIndicador', related_name='valor', on_delete=models.CASCADE)
    valor = models.CharField(("Valor"), max_length=50)
    class Meta:
        verbose_name = 'ValorVariable'
        verbose_name_plural = 'ValorVariables'

    def __str__(self):
        return f'{self.medicion} :{self.valor}'
