# Generated by Django 2.2.10 on 2020-02-26 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_reservations', '0002_confirmationlogs_num_people'),
    ]

    operations = [
        migrations.AddField(
            model_name='billingdraft',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]
