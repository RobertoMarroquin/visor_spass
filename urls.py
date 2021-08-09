from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'governmentpurchase', views.GovernmentPurchaseViewSet)
router.register(r'governmentinstitution', views.GovernmentInstitutionViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('supplier/<int:seller_id>/', views.SupplierSalesList.as_view()),
    path('jobs/<int:institution_id>/', views.JobsList.as_view()),
]
