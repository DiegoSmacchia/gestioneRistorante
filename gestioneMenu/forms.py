from django import forms
from django.core.validators import MinValueValidator
from django.forms import widgets
from django.forms.fields import BooleanField
from django.forms.models import ModelForm

from gestioneMenu.models import IngredientePiatto, Ingrediente

class IngredienteForm(ModelForm):
    class Meta:
        model = Ingrediente
        fields = ['nome', 'idMisura', 'fattoInCasa']
        labels = {
            'nome': 'Nome',
            'idMisura': 'Misura',
            'fattoInCasa':'Fatto in Casa'
        }

class PiattoForm(forms.Form):
    nome = forms.CharField(max_length=200)
    tempoPreparazione = forms.DecimalField(label ="Tempo di Preparazione (Minuti, maggiore o uguale a 0):",max_digits=15,decimal_places=2,validators=[MinValueValidator(0)])
    tempoCottura = forms.DecimalField(label ="Tempo di Cottura (Minuti, maggiore o uguale a 0):", max_digits=15,decimal_places=2,validators=[MinValueValidator(0)])

class IngredientePiattoForm(ModelForm):
    class Meta:
        model = IngredientePiatto
        fields = ['idPiatto', 'idIngrediente', 'quantita']
        labels ={
            'idPiatto':'Piatto: ',
            'idIngrediente':'Ingrediente: ',
            'quantita':'Quantità: '
        }
