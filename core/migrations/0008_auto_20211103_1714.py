# Generated by Django 3.2.7 on 2021-11-03 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20211103_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informacao_pessoal',
            name='plano_saude',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='informacao_pessoal',
            name='religiao',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='informacao_pessoal',
            name='reponsavel',
            field=models.CharField(max_length=50, null=True),
        ),
    ]