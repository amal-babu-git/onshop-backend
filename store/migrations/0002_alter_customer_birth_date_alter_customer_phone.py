# Generated by Django 4.0.5 on 2022-06-21 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
