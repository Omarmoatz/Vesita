from django.shortcuts import render
from .models import Doctor,Specialty,Comment,Examination
from django.views import generic
from .forms import ExaminationForm

class DoctorList(generic.ListView):
    model = Doctor

class DoctorDetail(generic.DetailView):
    model = Doctor

class BookExamination(generic.CreateView):
    model = Examination
    form_class = ExaminationForm
    success_url = '/'

