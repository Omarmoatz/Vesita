from django.urls import path
from .views import DoctorList,DoctorDetail


app_name = 'doctor'

urlpatterns = [
    path('',DoctorList.as_view(), name="doctor_list"),
    path('detail/<slug:slug>',DoctorDetail.as_view(), name="doctor_detail")
]

