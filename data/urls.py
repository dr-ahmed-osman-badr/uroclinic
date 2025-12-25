from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PatientViewSet, AdmissionViewSet, OperationViewSet, 
    OneDayInwardViewSet, LabsViewSet, ImagesViewSet, 
    ConsultationViewSet, CalenderAppointmentsViewSet, 
    ListOfDaysInwardViewSet
)

router = DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'admissions', AdmissionViewSet)
router.register(r'operations', OperationViewSet)
router.register(r'one-day-inward', OneDayInwardViewSet)
router.register(r'labs', LabsViewSet)
router.register(r'images', ImagesViewSet)
router.register(r'consultations', ConsultationViewSet)
router.register(r'appointments', CalenderAppointmentsViewSet)
router.register(r'list-of-days-inward', ListOfDaysInwardViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
