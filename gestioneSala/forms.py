from django.forms.models import ModelForm
from .models import ComponenteOrdine, Sala, Tavolo

class SalaForm(ModelForm):
    class Meta:
        model = Sala
        fields = ['nome']
        labels = {
            'nome': 'Nome: '
        }

class TavoloForm(ModelForm):
    class Meta:
        model = Tavolo
        fields = ['idSala', 'nome']
        labels = {
            'idSala' : 'Sala: ',
            'nome':'Nome (o Numero): '
        }

class ComponenteOrdineForm(ModelForm):
    class Meta:
        model = ComponenteOrdine
        fields = ['idPiatto', 'quantita', 'uscita', 'variazioni']
        labels = {
            'idPiatto' : 'Piatto: ',
            'quantita' : 'Quantità: ',
            'uscita' : 'Uscita: ',
            'variazioi': 'Variazioni'
        }