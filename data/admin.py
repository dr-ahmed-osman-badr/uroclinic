from django.contrib import admin
from .models import Patient, Admission,Operation,Labs,Images,Consultation, Calender_appointments, One_day_inward, List_of_days_inward

class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'serial_number', 'unique_id', 'gender', 'tel1')
    readonly_fields = ('unique_id', 'serial_number')
    search_fields = ('name', 'serial_number', 'unique_id', 'tel1')

admin.site.register(Patient, PatientAdmin)
admin.site.register(Admission)
admin.site.register(Operation)
admin.site.register(Labs)
admin.site.register(Images)
admin.site.register(Consultation)
admin.site.register(Calender_appointments)
admin.site.register(One_day_inward)
admin.site.register(List_of_days_inward)
