# Generated by Django 3.2 on 2022-02-13 09:48

import bookappointment.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookappointment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='appointment_date_and_time',
            field=models.DateTimeField(blank=True, null=True, validators=[bookappointment.models.Appointment.validate_date]),
        ),
    ]
