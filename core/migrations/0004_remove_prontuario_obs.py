# Generated by Django 3.2.7 on 2021-11-07 00:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20211106_2148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prontuario',
            name='obs',
        ),
    ]