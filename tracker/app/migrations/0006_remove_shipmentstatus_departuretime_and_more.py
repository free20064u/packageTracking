# Generated by Django 4.2.7 on 2024-07-30 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_shipmentstatus_receiveddate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shipmentstatus',
            name='departureTime',
        ),
        migrations.AlterField(
            model_name='shipmentstatus',
            name='expectedDeliveryDate',
            field=models.DateField(),
        ),
    ]
