# Generated by Django 4.2.7 on 2024-09-24 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_shipmentstatus_batch'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipmentstatus',
            name='barcode',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
