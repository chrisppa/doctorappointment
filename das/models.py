from django.db import models

class Appointment(models.Model):
    patientname = models.CharField(max_length=255)
    doctorname = models.CharField(max_length=255)
    date = models.DateField(null=True)
    details = models.CharField(max_length=255)

    def __str__(self):
       return "{self.doctorname} {self.date}"