from rest_framework import viewsets
from .models import (
    Patient, Admission, Operation, One_day_inward, Labs, Images, 
    Consultation, Calender_appointments, List_of_days_inward
)
from .serializers import (
    PatientSerializer, AdmissionSerializer, OperationSerializer, 
    OneDayInwardSerializer, LabsSerializer, ImagesSerializer, 
    ConsultationSerializer, CalenderAppointmentsSerializer, 
    ListOfDaysInwardSerializer
)

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class AdmissionViewSet(viewsets.ModelViewSet):
    queryset = Admission.objects.all()
    serializer_class = AdmissionSerializer

class OperationViewSet(viewsets.ModelViewSet):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer

class OneDayInwardViewSet(viewsets.ModelViewSet):
    queryset = One_day_inward.objects.all()
    serializer_class = OneDayInwardSerializer

class LabsViewSet(viewsets.ModelViewSet):
    queryset = Labs.objects.all()
    serializer_class = LabsSerializer

class ImagesViewSet(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer

class ConsultationViewSet(viewsets.ModelViewSet):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer

class CalenderAppointmentsViewSet(viewsets.ModelViewSet):
    queryset = Calender_appointments.objects.all()
    serializer_class = CalenderAppointmentsSerializer

class ListOfDaysInwardViewSet(viewsets.ModelViewSet):
    queryset = List_of_days_inward.objects.all()
    serializer_class = ListOfDaysInwardSerializer
