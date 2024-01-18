from django.shortcuts import render
from .models import Doctor,Specialty,Comment
from django.views import generic


class DoctorList(generic.ListView):
    model = Doctor


class DoctorDetail(generic.DetailView):
    model = Doctor

