from time import time
from django.db import models
from django.db.models.deletion import CASCADE
from django.core.validators import MinValueValidator
from gestioneMenu.models import Piatto

# Create your models here.
class Sala(models.Model):
    nome = models.CharField(max_length=50)
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = 'Sala'
        verbose_name_plural = 'Sale'

class Tavolo(models.Model):
    nome = models.CharField(max_length=50)
    idSala = models.ForeignKey(Sala, on_delete=CASCADE)
    inGestione = models.BooleanField(default=False)
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = 'Tavolo'
        verbose_name_plural = 'Tavoli'

class Stato(models.Model):
    nome = models.CharField(max_length=50)
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = 'Stato'
        verbose_name_plural = 'Stati'

class Ordine(models.Model):
    idTavolo = models.ForeignKey(Tavolo, on_delete=CASCADE)
    stato = models.ForeignKey(Stato, on_delete=CASCADE)
    uscitaAttuale = models.IntegerField(validators=[MinValueValidator(0)])
    orario = models.TimeField(null=True)
    class Meta:
        verbose_name = 'Ordine'
        verbose_name_plural = 'Ordini'

class ComponenteOrdine(models.Model):
    idOrdine = models.ForeignKey(Ordine, on_delete=CASCADE)
    idPiatto = models.ForeignKey(Piatto, on_delete=CASCADE)
    quantita = models.DecimalField(max_digits = 5, decimal_places = 2, validators=[MinValueValidator(0)])
    uscita = models.IntegerField(validators=[MinValueValidator(0)])
    variazioni = models.CharField(max_length=100)
    class Meta:
        verbose_name = 'ComponenteOrdine'
        verbose_name_plural = 'ComponentiOrdini'

class OrdineTemporaneo(models.Model):
    idTavolo = models.ForeignKey(Tavolo, on_delete=CASCADE)
    stato = models.ForeignKey(Stato, on_delete=CASCADE)
    uscitaAttuale = models.IntegerField(validators=[MinValueValidator(0)])
    orario = models.TimeField(null=True)
    class Meta:
        verbose_name = 'OrdineTemporaneo'
        verbose_name_plural = 'OrdiniTemporanei'

class ComponenteTemporaneo(models.Model):
    idOrdine = models.ForeignKey(OrdineTemporaneo, on_delete=CASCADE)
    idPiatto = models.ForeignKey(Piatto, on_delete=CASCADE)
    quantita = models.DecimalField(max_digits = 5, decimal_places = 2, validators=[MinValueValidator(0)])
    uscita = models.IntegerField(validators=[MinValueValidator(0)])
    variazioni = models.CharField(max_length=100)
    class Meta:
        verbose_name = 'ComponenteTemporaneo'
        verbose_name_plural = 'ComponentiTemporanei'