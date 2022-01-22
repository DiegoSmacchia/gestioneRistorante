from tkinter import CASCADE
from django.db import models
from django.core.validators import MinValueValidator
from gestioneMenu.models import Ingrediente

# Create your models here.
class Scorta(models.Model):
    idIngrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)
    quantitaAttuale = models.FloatField(validators=[MinValueValidator(0)])
    quantitaMinima = models.FloatField(validators=[MinValueValidator(0)])
    def __str__(self):
        return self.idIngrediente
    class Meta:
        verbose_name = 'Scorta'
        verbose_name_plural = 'Scorte'
    
class Spesa(models.Model):
    idIngrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)
    quantita = models.FloatField(validators=[MinValueValidator(0)])
    def __str__(self):
        return self.idIngrediente
    class Meta:
        verbose_name = 'Spesa'
        verbose_name_plural = 'Spese'

class Preparazione(models.Model):
    idIngrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)
    quantita = models.FloatField(validators=[MinValueValidator(0)])
    def __str__(self):
        return self.idIngrediente
    class Meta:
        verbose_name = 'Preparazione'
        verbose_name_plural = 'Preparazioni'