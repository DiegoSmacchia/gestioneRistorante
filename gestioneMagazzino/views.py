from msilib.schema import Error
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import ScortaForm
from .models import Preparazione, Scorta, Spesa

# Create your views here.
@login_required
def gestioneMagazzino(request):
    return render(request, "gestioneMagazzino.html")

@login_required
def scorte(request):
    form = ScortaForm()
    scorte = Scorta.objects.all()
    return render(request, 'scorte/scorte.html', {'form':form,'scorte':scorte, 'permessiAzioni': request.user.has_perm('gestioneMenu.delete_Scorta') })

@login_required
def tabellaScorte(request):
    scorte = Scorta.objects.all()
    return render(request, 'scorte/tabellaScorte.html', {'scorte' : scorte,'permessiAzioni': request.user.has_perm('gestioneMenu.delete_Scorta')})

@login_required
def nuovaScorta(request):
    if request.method == 'POST':
        form = ScortaForm(request.POST)
        
        if form.is_valid():
            
            nuovaScorta = Scorta(idIngrediente = form.cleaned_data['idIngrediente'], 
                                quantitaAttuale = form.cleaned_data['quantitaAttuale'], 
                                quantitaMinima = form.cleaned_data['quantitaMinima'])
            nuovaScorta.save()
            return render(request, 'operazioneRiuscita.html', {'messaggio':"Inserimento Riuscito!"})
        else:
            print(form)
            return render(request, 'operazioneFallita.html', {'messaggio':"Inserimento fallito, ricontrollare i campi!"})
    else:      
        return Error

@login_required()
def modificaScorta(request):
    if request.method == 'POST':
        idScorta = request.POST['idScorta']
        scorta = Scorta.objects.get(id=idScorta)
        form = ScortaForm(initial={'idIngrediente':scorta.idIngrediente, 'quantitaAttuale':scorta.quantitaAttuale, 'quantitaMinima':scorta.quantitaMinima})

        return render(request, 'scorte/modificaScorta.html', {'idScorta':idScorta, 'form':form})
    else:
        return Error

@login_required
def applicaModificheScorta(request):
    if request.method == 'POST':
        form = ScortaForm(request.POST)
        idSscorta = request.POST['idScorta']
        if form.is_valid():
            scorta = Scorta.objects.get(id=idSscorta)
            scorta.idIngrediente = form.cleaned_data['idIngrediente']
            scorta.quantitaAttuale = form.cleaned_data['quantitaAttuale']
            scorta.quantitaMinima = form.cleaned_data['quantitaMinima']
            scorta.save()
            return render(request, 'operazioneRiuscita.html', {'messaggio':"Modifica Riuscita!"})
        else:
            return render(request, 'operazioneFallita.html', {'messaggio':"Modifica fallita, ricontrollare i campi!"})
    else:
        return Error
    
@login_required
def eliminaScorta(request):
    if request.method == 'POST':
        idScorta = request.POST['idScorta']
        scorta = Scorta.objects.get(id=idScorta)
        scorta.delete()
        return render(request, 'operazioneRiuscita.html', {'messaggio':"Ingrediente Eliminato!"})
    else:
        return Error


#Spese
@login_required
def spese(request):
    spese = Spesa.objects.all()
    return render(request, 'spese/tabellaSpese.html', {'spese':spese, 'permessiAzioni': request.user.has_perm('gestioneMenu.delete_Scorta') })


#Preparazioni
@login_required
def preparazioni(request):
    preparazioni = Preparazione.objects.all()
    return render(request, 'preparazioni/tabellaPreparazioni.html', {'preparazioni':preparazioni, 'permessiAzioni': request.user.has_perm('gestioneMenu.delete_Scorta') })
