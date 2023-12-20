from django.contrib import admin
from .models import Appointment

# Register your models here.
class AppointmentAdmin(admin.ModelAdmin):
  list_display = ("doctorname", "patientname", "date", "details")
  
admin.site.register(Appointment, AppointmentAdmin)
