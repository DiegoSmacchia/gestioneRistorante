# Generated by Django 3.2.9 on 2022-01-25 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestioneMenu', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='piatto',
            name='tempoCottura',
        ),
        migrations.RemoveField(
            model_name='piatto',
            name='tempoPreparazione',
        ),
    ]
