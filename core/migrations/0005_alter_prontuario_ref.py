# Generated by Django 3.2.7 on 2021-10-31 00:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_prontuario_ref'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prontuario',
            name='ref',
            field=models.CharField(default=datetime.date(2021, 10, 31), max_length=200),
        ),
    ]