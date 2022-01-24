from aifc import Error
from datetime import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from gestioneSala.models import Ordine, ComponenteOrdine, Stato
# Create your views here.
@login_required
def gestioneCucina(request):
    return render(request, 'gestioneCucina.html')

@login_required
def contenutoCucina(request):
    ordini = Ordine.objects.all().order_by('orario')
    orarioPrimoOrdine = datetime.strptime(str(ordini.first().orario), '%H:%M:%S.%f')
    componentiInAttesa = ComponenteOrdine.objects.filter(stato = Stato.objects.get(id = 1))
    componentiInPreparazione = ComponenteOrdine.objects.filter(stato = Stato.objects.get(id = 2))

    for componente in componentiInAttesa:
        orarioOrdine = datetime.strptime(str(ordini.get(id = componente.idOrdine.id).orario), '%H:%M:%S.%f')
        componente.priorita = (1 + (orarioPrimoOrdine - orarioOrdine).total_seconds() ) * componente.uscita
    componentiInAttesa.order_by('priorita')

    ordiniInPreparazione = []
    for componente in componentiInPreparazione:
        if(not ordiniInPreparazione.__contains__(componente.idOrdine) ):
            ordiniInPreparazione.append(componente.idOrdine)
    
    return render(request, 'contenutoCucina.html', {'ordiniinpreparazione':ordiniInPreparazione, 'componentiinpreparazione':componentiInPreparazione, 'componentiinattesa':componentiInAttesa})


@login_required
def componenteServito(request):
    if request.method == 'POST':
        idComponente = request.POST['idComponente']
        componente = ComponenteOrdine.objects.get(id = idComponente)
        componente.stato = Stato.objects.get(id = 3)
        componente.save()
        return render(request, 'operazioneRiuscita.html', {'messaggio':'componente segnato come servito!'})
    else:
        return Error

def inizioPreparazioneComponente(request):
    if request.method == 'POST':
        idComponente = request.POST['idComponente']
        componente = ComponenteOrdine.objects.get(id = idComponente)
        componente.stato = Stato.objects.get(id = 2)
        componente.save()
        return render(request, 'operazioneRiuscita.html', {'messaggio':'componente segnato come servito!'})
    else:
        return Error
