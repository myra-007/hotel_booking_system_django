# Generated by Django 2.2.10 on 2020-02-26 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MealPlans',
            fields=[
                ('s_no', models.AutoField(primary_key=True, serialize=False)),
                ('plan_name', models.CharField(max_length=100)),
                ('alias_name', models.CharField(max_length=1)),
                ('descr', models.TextField()),
                ('date_added', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'meal_plans',
            },
        ),
    ]
