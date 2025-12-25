from rest_framework import serializers
from .models import (
    Patient, Admission, Operation, One_day_inward, Labs, Images, 
    Consultation, Calender_appointments, List_of_days_inward
)

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
        read_only_fields = ['unique_id', 'serial_number']

class AdmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admission
        fields = '__all__'

class OperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operation
        fields = '__all__'

class OneDayInwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = One_day_inward
        fields = '__all__'

class LabsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Labs
        fields = '__all__'

class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = '__all__'

class ConsultationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultation
        fields = '__all__'

class CalenderAppointmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calender_appointments
        fields = '__all__'

class ListOfDaysInwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = List_of_days_inward
        fields = '__all__'
