from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse

from rest_framework import viewsets, generics
from .serializers import GovernmentPurchaseSerializer, SupplierSerializer, JobSerializer, GovernmentInstitutionSerializer
from .models import GovernmentPurchase, Person, Job, GovernmentInstitution

from .forms import ComplaintForm
from .models import Complaint


class ComplaintCreateView(CreateView):
    model = Complaint
    template_name = "cacao/denuncia.html"
    form_class = ComplaintForm
    def get_success_url(self,**kwargs):
        return reverse('denuncia')

class GovernmentPurchaseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = GovernmentPurchase.objects.all()
    serializer_class = GovernmentPurchaseSerializer

class GovernmentInstitutionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = GovernmentInstitution.objects.all()
    serializer_class = GovernmentInstitutionSerializer

class SupplierSalesList(generics.ListAPIView):
    serializer_class = GovernmentPurchaseSerializer

    def get_queryset(self):
        seller = self.kwargs['seller_id']
        return GovernmentPurchase.objects.filter(seller=seller)

class JobsList(generics.ListAPIView):
    serializer_class = JobSerializer

    def get_queryset(self):
        institution = self.kwargs['institution_id']
        return Job.objects.filter(government_institution=institution)
