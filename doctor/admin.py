from django.contrib import admin
from .models import Doctor,Specialty,Comment,ClinicPhoto,Examination

class clinicTabular(admin.TabularInline):
    model = ClinicPhoto

class DoctorAdmin(admin.ModelAdmin):
    inlines = [clinicTabular]
    list_filter = ['price_of_appintment','specialty']

admin.site.register(Doctor,DoctorAdmin)
admin.site.register(Specialty)
admin.site.register(Comment)
admin.site.register(Examination)