# Generated by Django 3.2.9 on 2022-01-21 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestioneSala', '0008_ordine_orario'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordinetemporaneo',
            name='orario',
            field=models.TimeField(null=True),
        ),
    ]
