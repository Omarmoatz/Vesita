# Generated by Django 5.0.1 on 2024-01-18 00:37

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0003_remove_doctor_comment_comment_doctor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='doctor_review',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='work_hours',
            field=models.PositiveIntegerField(),
        ),
        migrations.CreateModel(
            name='ClinicPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='clinic_img/')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clinic_doctor', to='doctor.doctor')),
            ],
        ),
    ]