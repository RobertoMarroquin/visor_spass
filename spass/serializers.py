from rest_framework import serializers
from .models import GovernmentPurchase, Job, GovernmentInstitution

class GovernmentPurchaseSerializer(serializers.ModelSerializer):
    government_institution_id = serializers.SlugRelatedField(source='government_institution', read_only=True, slug_field='id')
    government_institution = serializers.StringRelatedField()
    seller = serializers.StringRelatedField()
    seller_id = serializers.SlugRelatedField(source='seller', read_only=True, slug_field='id')
    purchase_order = serializers.StringRelatedField()
    purchase_order_url = serializers.SlugRelatedField(source='purchase_order', read_only=True, slug_field='url')
    class Meta:
        model = GovernmentPurchase
        fields = ['id','government_institution_id','government_institution','seller','description','award_date',
        'price','purchase_order', 'purchase_order_url', 'seller_id']

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = GovernmentPurchase
        fields = ['id','government_institution_id','government_institution','seller','description','award_date',
        'price','purchase_order']

class GovernmentInstitutionSerializer(serializers.ModelSerializer):
    name = serializers.StringRelatedField()
    class Meta:
        model = GovernmentInstitution
        fields = ['id','name']

class JobSerializer(serializers.ModelSerializer):
    natural_person = serializers.CharField(source='natural_person.complete_name')
    class Meta:
        model = Job
        fields = ['id','job_name','nominal_job_name','natural_person','monthly_salary','start_date','academic_degree',
        'work_area']
