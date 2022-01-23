# Generated by Django 3.2.9 on 2022-01-15 10:11

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gestioneMenu', '0018_remove_piatto_tempototale'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Sala',
                'verbose_name_plural': 'Sale',
            },
        ),
        migrations.CreateModel(
            name='Stato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Stato',
                'verbose_name_plural': 'Stati',
            },
        ),
        migrations.CreateModel(
            name='Tavolo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('idSala', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestioneSala.sala')),
            ],
            options={
                'verbose_name': 'Tavolo',
                'verbose_name_plural': 'Tavoli',
            },
        ),
        migrations.CreateModel(
            name='Ordine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uscitaAttuale', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('Stato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestioneSala.stato')),
                ('idTavolo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestioneSala.tavolo')),
            ],
        ),
        migrations.CreateModel(
            name='ComponenteOrdine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantita', models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(0)])),
                ('uscita', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('variazioni', models.CharField(max_length=100)),
                ('idOrdine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestioneSala.ordine')),
                ('idPiatto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestioneMenu.piatto')),
            ],
        ),
    ]