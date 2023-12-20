from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Appointment

def home(request):
   template = loader.get_template('homepage.html')
   return HttpResponse(template.render())

def appointments(request):
   myappointments = Appointment.objects.all().values()
   template = loader.get_template('appointments.html'),
   context = {
      'myappointments': myappointments,
   }
   return render(request, 'appointments.html', context=context)
