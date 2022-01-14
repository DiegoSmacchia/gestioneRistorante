from django import forms
from django.core.validators import MinValueValidator
from django.forms.models import ModelForm

from gestioneMenu.models import IngredientePiatto, Ingrediente, Menu, Piatto

class IngredienteForm(ModelForm):
    class Meta:
        model = Ingrediente
        fields = ['nome', 'idMisura', 'fattoInCasa']
        labels = {
            'nome': 'Nome',
            'idMisura': 'Misura',
            'fattoInCasa':'Fatto in Casa'
        }

class PiattoForm(ModelForm):
    class Meta:
        model = Piatto
        fields = ['nome', 'idCategoria', 'tempoPreparazione', 'tempoCottura']
        labels = {
            'nome':'Nome: ',
            'idCategoria':'Categoria: ',
            'tempoPreparazione':'Tempo di preparazione: ',
            'tempoCottura':'Tempo di cottura: '
        }

class IngredientePiattoForm(ModelForm):
    class Meta:
        model = IngredientePiatto
        fields = ['idPiatto', 'idIngrediente', 'quantita']
        labels = {
            'idPiatto':'Piatto: ',
            'idIngrediente':'Ingrediente: ',
            'quantita':'Quantità: '
        }

class MenuForm(ModelForm):
    class Meta:
        model = Menu
        fields = ['idPiatto', 'descrizione', 'prezzo']
        labels = {
            'idPiatto':'Piatto: ',
            'descrizione':'Descrizione: ',
            'prezzo':'prezzo: '
        }