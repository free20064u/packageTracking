# Generated by Django 4.2.7 on 2024-06-23 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_package_shipmentstatus_batch_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipmenthistory',
            name='carrierReferenceNo',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='shipmenthistory',
            name='updatedBy',
            field=models.CharField(default='admin', max_length=100),
        ),
    ]
