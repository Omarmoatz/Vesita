from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator,RegexValidator
from phonenumber_field.modelfields import PhoneNumberField

class Doctor(models.Model):
    name = models.CharField( max_length=50)
    image = models.ImageField( upload_to='doctor/')
    address = models.CharField( max_length=200)
    specialty = models.ForeignKey("Specialty", related_name="specialty_doctor", on_delete=models.SET_NULL,blank=True, null=True)
    subtitle = models.TextField(max_length=200)
    description = models.TextField(max_length=2000)
    price_of_appintment = models.PositiveIntegerField(default=None)
    phone_num = models.CharField( max_length=50)
    work_hours = models.PositiveIntegerField()
    doctor_review = models.PositiveIntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)])
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
       self.slug = slugify(self.name)
       super(Doctor, self).save(*args, **kwargs) 

    class Meta:
        ordering = ['-id']

class ClinicPhoto(models.Model):
    doctor = models.ForeignKey(Doctor, related_name="clinic_doctor", on_delete=models.CASCADE)
    image = models.ImageField( upload_to='clinic_img/')

    def __str__(self):
        return str(self.doctor)


class Specialty(models.Model):
    name = models.CharField( max_length=100)

    def __str__(self):
        return self.name

class Comment(models.Model):
    user = models.ForeignKey(User, related_name='user_comment', on_delete=models.CASCADE)
    content = models.TextField(max_length=500)
    created_at = models.DateTimeField(default=timezone.now)
    doctor = models.ForeignKey(Doctor, related_name="comment_doctor", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)
    

GENDER_CHOICE = (
    ('Male','Male'),
    ('Female','Female'),
)
class Examination(models.Model):
    name = models.CharField( max_length=50)
    age = models.PositiveIntegerField(blank=True, null=True)
    gender = models.CharField( max_length=50, choices=GENDER_CHOICE)
    phone = PhoneNumberField()
    email = models.EmailField( max_length=254,blank=True, null=True)
    symptoms = models.TextField(max_length=5000)
    examination_date = models.DateTimeField(default=timezone.now)
