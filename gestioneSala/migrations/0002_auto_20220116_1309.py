# Generated by Django 3.2.9 on 2022-01-16 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestioneSala', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='componenteordine',
            options={'verbose_name': 'Componenterdine', 'verbose_name_plural': 'ComponentiOrdini'},
        ),
        migrations.AlterModelOptions(
            name='ordine',
            options={'verbose_name': 'Ordine', 'verbose_name_plural': 'Ordini'},
        ),
    ]