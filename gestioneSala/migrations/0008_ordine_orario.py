# Generated by Django 3.2.9 on 2022-01-21 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestioneSala', '0007_tavolo_ingestione'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordine',
            name='orario',
            field=models.TimeField(null=True),
        ),
    ]