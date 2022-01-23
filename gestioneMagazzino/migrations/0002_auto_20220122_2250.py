# Generated by Django 3.2.9 on 2022-01-22 21:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestioneMenu', '0018_remove_piatto_tempototale'),
        ('gestioneMagazzino', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preparazione',
            name='idIngrediente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestioneMenu.ingrediente', unique=True),
        ),
        migrations.AlterField(
            model_name='scorta',
            name='idIngrediente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestioneMenu.ingrediente', unique=True),
        ),
        migrations.AlterField(
            model_name='spesa',
            name='idIngrediente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestioneMenu.ingrediente', unique=True),
        ),
    ]