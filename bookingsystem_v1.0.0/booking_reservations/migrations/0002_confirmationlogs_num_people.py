# Generated by Django 2.2.10 on 2020-02-26 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_reservations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='confirmationlogs',
            name='num_people',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
