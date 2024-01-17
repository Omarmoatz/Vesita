from django.urls import path
from .views import DoctorList


app_name = 'doctor'

urlpatterns = [
    path('',DoctorList.as_view(), name="doctor_list")
]

