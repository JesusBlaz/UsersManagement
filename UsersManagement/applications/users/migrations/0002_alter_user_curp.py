# Generated by Django 4.0.6 on 2022-07-27 05:26

import curp.exceptions
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='curp',
            field=models.CharField(max_length=18, validators=[curp.exceptions.CURPValueError]),
        ),
    ]