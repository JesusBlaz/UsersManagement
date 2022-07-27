# Generated by Django 4.0.6 on 2022-07-27 05:31

import applications.users.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_curp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='curp',
            field=models.CharField(max_length=18, validators=[applications.users.validators.curp_validation]),
        ),
    ]
