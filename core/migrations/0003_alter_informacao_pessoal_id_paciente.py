# Generated by Django 3.2.7 on 2021-10-24 19:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_alter_agendamento_data_hora'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informacao_pessoal',
            name='id_paciente',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
