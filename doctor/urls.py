from django.urls import path
from .views import DoctorList,DoctorDetail,BookExamination


app_name = 'doctor'

urlpatterns = [
    path('',DoctorList.as_view(), name="doctor_list"),
    path('detail/<slug:slug>',DoctorDetail.as_view(), name="doctor_detail"),
    path('detail/<slug:slug>/book_ex',BookExamination.as_view(), name="examination"),
]

