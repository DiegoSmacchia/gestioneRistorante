# Generated by Django 3.2.9 on 2022-01-14 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestioneMenu', '0017_piatto_idcategoria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='piatto',
            name='tempoTotale',
        ),
    ]