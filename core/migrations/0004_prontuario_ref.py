# Generated by Django 3.2.7 on 2021-10-31 00:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_informacao_pessoal_id_paciente'),
    ]

    operations = [
        migrations.AddField(
            model_name='prontuario',
            name='ref',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
