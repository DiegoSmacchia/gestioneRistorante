from django.db import models
from django.core.validators import MinValueValidator

class Misura(models.Model):
    nome = models.TextField(max_length=50)
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = 'Misura'
        verbose_name_plural = 'Misure'

class Ingrediente(models.Model):
    nome = models.CharField(max_length=100)
    idMisura = models.ForeignKey(Misura, on_delete=models.CASCADE)
    fattoInCasa = models.BooleanField()
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = 'Ingrediente'
        verbose_name_plural = 'Ingredienti'

class Piatto(models.Model):
    nome = models.CharField(max_length=200)
    tempoTotale = models.DecimalField(max_digits=15,decimal_places=2,validators=[MinValueValidator(0)])
    tempoPreparazione = models.DecimalField(max_digits=15,decimal_places=2,validators=[MinValueValidator(0)])
    tempoCottura = models.DecimalField(max_digits=15,decimal_places=2,validators=[MinValueValidator(0)])
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = 'Piatto'
        verbose_name_plural = 'Piatti'

class IngredientePiatto(models.Model):
    idPiatto = models.ForeignKey(Piatto, on_delete=models.CASCADE)
    idIngrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)
    quantita = models.FloatField(MinValueValidator(0))
    class Meta:
        verbose_name = 'IngredientePiatto'
        verbose_name_plural = 'IngredientiPiatti'