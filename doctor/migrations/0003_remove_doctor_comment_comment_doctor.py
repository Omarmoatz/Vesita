# Generated by Django 5.0.1 on 2024-01-17 16:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0002_remove_doctor_location_doctor_address_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='comment',
        ),
        migrations.AddField(
            model_name='comment',
            name='doctor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comment_doctor', to='doctor.doctor'),
            preserve_default=False,
        ),
    ]
