from django import forms
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError

class IngredienteForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    fattoInCasa = forms.BooleanField(required=False)
    def __init__(self, *args, **kwargs):
        super(IngredienteForm, self).__init__(*args, **kwargs)
        self.fields['fattoInCasa'].label = "Fatto In Casa:"

class PiattoForm(forms.Form):
    nome = forms.CharField(max_length=200)
    tempoPreparazione = forms.DecimalField(max_digits=15,decimal_places=2,validators=[MinValueValidator(0)])
    tempoCottura = forms.DecimalField(max_digits=15,decimal_places=2,validators=[MinValueValidator(0)])
    def __init__(self, *args, **kwargs):
        super(PiattoForm, self).__init__(*args, **kwargs)
        self.fields['tempoPreparazione'].label = "Tempo di Preparazione (Minuti, maggiore o uguale a 0):"
        self.fields['tempoCottura'].label = "Tempo di Cottura (Minuti, maggiore o uguale a 0):"
    def clean(self):
        tempoPrep = self.cleaned_data['tempoPreparazione']
        if tempoPrep < 0:
            raise ValidationError("Tempo di preparazione troppo basso!")
        tempoCott = self.cleaned_data['tempoCottura']
        if tempoCott < 0:
            raise ValidationError("Tempo di cottura troppo basso!")