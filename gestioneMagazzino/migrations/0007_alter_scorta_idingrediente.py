# Generated by Django 3.2.9 on 2022-01-23 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestioneMenu', '0018_remove_piatto_tempototale'),
        ('gestioneMagazzino', '0006_auto_20220123_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scorta',
            name='idIngrediente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestioneMenu.ingrediente'),
        ),
    ]
