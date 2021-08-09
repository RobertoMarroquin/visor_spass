from django.db import models
from django.contrib.auth.models import User


class NaturalPerson(models.Model):
    class Sex(models.TextChoices):
        HOMBRE = 'M','Hombre'
        MUJER = 'F','Mujer'

    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30,blank=True)
    third_name = models.CharField(max_length=30,blank=True)
    first_surname = models.CharField(max_length=30)
    second_surname = models.CharField(max_length=30,blank=True)
    third_surname = models.CharField(max_length=30,blank=True)
    married_name = models.CharField(max_length=30,blank=True)
    known_for_name = models.CharField(max_length=60,blank=True)
    known_for_surname = models.CharField(max_length=60,blank=True)
    dui = models.PositiveIntegerField(("DUI"),unique=True,blank=True,null=True)
    verification_dui_digit = models.PositiveSmallIntegerField(("Dígito verificador del DUI"),blank=True,null=True)
    nit = models.CharField(("NIT"),max_length=14,blank=True)
    biological_sex = models.CharField(max_length=1,choices=Sex.choices,default=Sex.HOMBRE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    created_by = models.ForeignKey(User,editable=False,null=True,blank=True, on_delete=models.CASCADE, related_name='NaturalPerson_created_by')
    updated_by = models.ForeignKey(User,editable=False,null=True,blank=True, on_delete=models.CASCADE, related_name='NaturalPerson_updated_by')

    class Meta:
        verbose_name = "Persona natural"
        verbose_name_plural = "Personas naturales"

    def complete_dui(self):
        return str(self.dui).zfill(8)+'-'+str(self.verification_dui_digit)

    def complete_name(self):
        if self.married_name == '':
            return self.first_name + " " + self.second_name + " " + self.first_surname + " " + self.second_surname
        else:
            return self.first_name + " " + self.second_name + " " + self.first_surname + " " + self.second_surname + " DE " + self.married_name

    def __str__(self):
        if self.dui is not None:
            return (self.complete_name() + ' - ' +
            'DUI: '+str(self.dui).zfill(8)+'-'+str(self.verification_dui_digit).zfill(1))
        else:
            return (self.complete_name() +
            ' - '+'DUI: No disponible')

class LegalPerson(models.Model):
    name = models.CharField(max_length=255)
    abbreviation = models.CharField(max_length=255,blank=True)
    tipo = models.ForeignKey('LegalType',on_delete=models.CASCADE)
    nit = models.CharField(max_length=14,blank=True)
    fecha_constitucion = models.DateField(blank=True,null=True)
    fecha_aprobacion = models.DateField(blank=True,null=True)
    fecha_matricula = models.DateField(blank=True,null=True)
    entidad_aprueba = models.ForeignKey('GovernmentInstitution', verbose_name="Entidad que aprobó",on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    created_by = models.ForeignKey(User,editable=False,null=True,blank=True, on_delete=models.CASCADE, related_name='LegalPerson_created_by')
    updated_by = models.ForeignKey(User,editable=False,null=True,blank=True, on_delete=models.CASCADE, related_name='LegalPerson_updated_by')

    class Meta:
        verbose_name = "Persona jurídica"
        verbose_name_plural = "Personas jurídicas"

    def complete_name(self):
        return self.abbreviation + " " + self.tipo.abbreviation

    def __str__(self):
        return self.abbreviation +', '+ self.tipo.abbreviation

class LegalType(models.Model):
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Tipo de persona jurídica'
        verbose_name_plural = 'Tipos de personas jurídicas'

    def __str__(self):
        return self.name

class GovernmentInstitution(models.Model):
    name = models.CharField(max_length=255)
    official_email = models.EmailField(("Correo del oficial"),null=True,blank=True)
    sector = models.ForeignKey('GovernmentSector', on_delete=models.CASCADE, verbose_name=("Sector"))
    created_by = models.ForeignKey(User,editable=False,null=True,blank=True, on_delete=models.CASCADE, related_name='GovernmentInstitution_created_by')
    updated_by = models.ForeignKey(User,editable=False,null=True,blank=True, on_delete=models.CASCADE, related_name='GovernmentInstitution_updated_by')

    class Meta:
        verbose_name = 'Institución de gobierno'
        verbose_name_plural = 'Instituciones de gobierno'

    def __str__(self):
        return self.name

class GovernmentSector(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Sector gubernamental'
        verbose_name_plural = 'Sectores gubernamentales'

    def __str__(self):
        return self.name

class Job(models.Model):

    job_name = models.CharField(("Cargo funcional"),max_length=100, blank=True, null=True)
    nominal_job_name = models.CharField(("Plaza nominal"),max_length=100, blank=True, null=True)
    academic_degree = models.CharField(("Grado académico reportado"),max_length=100, blank=True, null=True)
    natural_person = models.ForeignKey("cacao.NaturalPerson", verbose_name=("Persona Natural"), on_delete=models.CASCADE)
    government_institution = models.ForeignKey(("cacao.GovernmentInstitution"), verbose_name=("Institucion del Estado"), on_delete=models.CASCADE, null=True, blank=True)
    monthly_salary = models.DecimalField(("Salario mensual"),max_digits=7,decimal_places=2,blank=True,null=True)
    start_date = models.DateField(("Inicio de la relación"),blank=True,null=True)
    end_date = models.DateField(("Finalización de la relación"),blank=True,null=True)
    work_area = models.CharField(("Área de Trabajo"), max_length=100,blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    created_by = models.ForeignKey(User,editable=False,null=True,blank=True, on_delete=models.CASCADE, related_name='Job_created_by')
    updated_by = models.ForeignKey(User,editable=False,null=True,blank=True, on_delete=models.CASCADE, related_name='Job_updated_by')

    class Meta:

        verbose_name = 'Puesto de trabajo'
        verbose_name_plural = 'Puestos de trabajo'

    def __str__(self):
        return f"{self.job_name}"

class Person(models.Model):
    class Type(models.TextChoices):
        NATURAL = 'N',"Persona natural"
        LEGAL = "L","Persona jurídica"

    person_type = models.CharField(max_length=1,choices=Type.choices,default=Type.NATURAL)
    natural_person_id = models.ForeignKey("cacao.NaturalPerson", on_delete=models.CASCADE, null=True, blank=True)
    legal_person_id = models.ForeignKey("cacao.LegalPerson", on_delete=models.CASCADE, null=True, blank=True)
    created_by = models.ForeignKey(User,editable=False,null=True,blank=True, on_delete=models.CASCADE, related_name='Person_created_by')
    updated_by = models.ForeignKey(User,editable=False,null=True,blank=True, on_delete=models.CASCADE, related_name='Person_updated_by')

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'

    def complete_name(self):
        if self.natural_person_id == None:
            if self.legal_person_id.abbreviation != '':
                return self.legal_person_id.abbreviation + ", " + self.legal_person_id.tipo.abbreviation
            else:
                return self.legal_person_id.name + ", " + self.legal_person_id.tipo.abbreviation
        else:
            return self.natural_person_id.complete_name()

    def __str__(self):
        if self.natural_person_id == None:
            return self.legal_person_id.abbreviation + ", " + self.legal_person_id.tipo.abbreviation
        else:
            return self.natural_person_id.complete_name()

class GovernmentPurchase(models.Model):
    government_institution = models.ForeignKey("cacao.GovernmentInstitution", on_delete=models.CASCADE)
    seller = models.ForeignKey("cacao.Person", on_delete=models.CASCADE)
    description = models.TextField()
    award_date = models.DateField()
    price = models.DecimalField(("Precio"),max_digits=11,decimal_places=2,blank=True,null=True)
    modality = models.ForeignKey("cacao.Modality", on_delete=models.CASCADE,blank=True,null=True)
    funding_source = models.ForeignKey("cacao.FundingSource", on_delete=models.CASCADE,blank=True,null=True)
    purchase_order = models.ForeignKey("cacao.PurchaseOrder", on_delete=models.CASCADE,blank=True,null=True)
    internal_code = models.CharField(max_length=100,blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    created_by = models.ForeignKey(User,editable=False,null=True,blank=True, on_delete=models.CASCADE, related_name='GovernmentPurchase_created_by')
    updated_by = models.ForeignKey(User,editable=False,null=True,blank=True, on_delete=models.CASCADE, related_name='GovernmentPurchase_updated_by')

    class Meta:
        verbose_name = 'Compra pública'
        verbose_name_plural = 'Compras públicas'

    def __str__(self):
        return self.government_institution.name + " - " + self.internal_code

class PurchaseOrder(models.Model):
    code = models.CharField(max_length=50)
    government_institution = models.ForeignKey("cacao.GovernmentInstitution", on_delete=models.CASCADE)
    url = models.URLField(blank=True)
    file_name = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    created_by = models.ForeignKey(User,editable=False,null=True,blank=True, on_delete=models.CASCADE, related_name='PurchaseOrder_created_by')
    updated_by = models.ForeignKey(User,editable=False,null=True,blank=True, on_delete=models.CASCADE, related_name='PurchaseOrder_updated_by')

    class Meta:

        verbose_name = 'Órden de compra'
        verbose_name_plural = 'Órdenes de compra'

    def __str__(self):
        return self.code +" - "+ self.government_institution.name

class FundingSource(models.Model):
    name = models.CharField(max_length=75)

    class Meta:

        verbose_name = 'Fuente de financiamiento'
        verbose_name_plural = 'Fuentes de financiamiento'

    def __str__(self):
        return self.name

class Modality(models.Model):
    name = models.CharField(max_length=75)

    class Meta:

        verbose_name = 'Modalidad de contratación'
        verbose_name_plural = 'Modalidades de contratación'

    def __str__(self):
        return self.name

class Complaint(models.Model):
    category        = models.IntegerField(("Categoria"),choices=[
        (1,"Compra Publica"),
        (2,"Institucion de Gobierno"),
        (3,"Persona Juridica"),
        (4,"Persona Natural"),
        (5,"Mixta")])
    gov_purchase    = models.ForeignKey("cacao.GovernmentPurchase",verbose_name=("Compra Publica"), on_delete=models.CASCADE,blank=True, null=True)
    gov_institution = models.ForeignKey('cacao.GovernmentInstitution',verbose_name=("Institucion de Govierno"), on_delete=models.CASCADE,blank=True, null=True)
    legal_person    = models.ForeignKey("cacao.LegalPerson", verbose_name=("Persona Juridica"), on_delete=models.CASCADE,blank=True, null=True)
    natural_person  = models.ForeignKey("cacao.NaturalPerson", verbose_name=("Persona Natural"), on_delete=models.CASCADE,blank=True, null=True)
    complaint       = models.TextField(("Denuncia"))
    created_at      = models.DateField(auto_now_add=True)
    updated_at      = models.DateField(auto_now=True)

    class Meta:
        verbose_name = ("Complaint")
        verbose_name_plural = ("Complaints")

    def __str__(self):
        return f"{self.id}:{self.category}:{self.created_at}"
