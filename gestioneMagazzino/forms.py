from django.forms.models import ModelForm

from .models import Scorta


class ScortaForm(ModelForm):
    class Meta:
        model = Scorta
        fields = ['idIngrediente', 'quantitaAttuale', 'quantitaMinima']
        labels = {
            'idIngrediente': 'Ingrediente: ',
            'quantitaAttuale': 'Quantità attuale: ',
            'quantitaMinima':'Quantità minima: '
        }
