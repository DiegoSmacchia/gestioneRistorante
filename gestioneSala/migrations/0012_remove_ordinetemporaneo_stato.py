# Generated by Django 3.2.9 on 2022-01-23 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestioneSala', '0011_auto_20220122_0958'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordinetemporaneo',
            name='stato',
        ),
    ]
