from msilib.schema import Error
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from numpy import identity

from .forms import ScortaForm
from .models import Preparazione, Scorta, Spesa

# Create your views here.
@login_required
def gestioneMagazzino(request):
    return render(request, "gestioneMagazzino.html")

@login_required
def scorte(request):
    form = ScortaForm()
    return render(request, 'scorte/scorte.html', {'form':form, 'permessiAzioni': request.user.has_perm('gestioneMenu.delete_Scorta') })

@login_required
def tabellaScorte(request):
    scorte = Scorta.objects.all()
    return render(request, 'scorte/tabellaScorte.html', {'scorte' : scorte,'permessiAzioni': request.user.has_perm('gestioneMenu.delete_Scorta')})

@login_required
def nuovaScorta(request):
    if request.method == 'POST':
        form = ScortaForm()
        return render(request, "scorte/formScorta.html", {'idScorta':0, 'form':form, 'oggetto':'Inserimento'})
    else:      
        return Error

@login_required()
def modificaScorta(request):
    if request.method == 'POST':
        idScorta = request.POST['idScorta']
        scorta = Scorta.objects.get(id=idScorta)
        form = ScortaForm(initial={'idIngrediente':scorta.idIngrediente, 'quantitaAttuale':scorta.quantitaAttuale, 'quantitaMinima':scorta.quantitaMinima})

        return render(request, 'scorte/formScorta.html', {'idScorta':idScorta, 'form':form, 'oggetto':'Modifica'})
    else:
        return Error

@login_required
def applicaInserimentoModificaScorta(request):
    if request.method == 'POST':
        form = ScortaForm(request.POST)
        idScorta = request.POST['idScorta']
        print(form)
        if form.is_valid():
            if idScorta == '0':
                try:
                    scortaEsistente = Scorta.objects.get(idIngrediente = form.cleaned_data['idIngrediente'])
                    if scortaEsistente is not None:
                        return render(request, 'operazioneFallita.html', {'messaggio':"Inserimento fallito, ingrediente già presente!"})
                except Scorta.DoesNotExist:
                    scorta = Scorta()
            else:
                scorta = Scorta.objects.get(id=idScorta)
                if scorta.idIngrediente != form.cleaned_data['idIngrediente']:
                    scortaEsistente = Scorta.objects.filter(idIngrediente = form.cleaned_data['idIngrediente'])
                    if scortaEsistente.count() > 0:
                        return render(request, 'operazioneFallita.html', {'messaggio':"Modifica fallita, ingrediente già presente!"})
      
            scorta.idIngrediente = form.cleaned_data['idIngrediente']
            scorta.quantitaAttuale = form.cleaned_data['quantitaAttuale']
            scorta.quantitaMinima = form.cleaned_data['quantitaMinima']

            scorta.save()
            aggiornaListe(scorta)
            return render(request, 'operazioneRiuscita.html', {'messaggio':"Operazione Riuscita!"})
        else:
            return render(request, 'operazioneFallita.html', {'messaggio':"Operazione fallita, ricontrollare i campi!"})
    else:
        return Error
    
@login_required
def confirmEliminaScorta(request):
    if request.method =='POST':
        return render(request, 'contenutoDialogConfirm.html', {'titolo':'Conferma Eliminazione', 
                                                            'contenuto':'Vuoi davvero eliminare questa scorta?', 
                                                            'urlrichiesto':'eliminaScorta', 
                                                            'hxtarget':'#divNotifica',
                                                            'parametro':request.POST['idScorta'],
                                                            'nomeparametro':'idScorta'})
    else:
        return Error

@login_required
def eliminaScorta(request):
    if request.method == 'POST':
        idScorta = request.POST['idScorta']
        scorta = Scorta.objects.get(id=idScorta)
        scorta.delete()
        return render(request, 'operazioneRiuscita.html', {'messaggio':"Scorta Eliminata!"})
    else:
        return Error

#Spese
@login_required
def spese(request):
    return render(request, 'spese/spese.html')

@login_required
def tabellaSpese(request):
    spese = Spesa.objects.all()
    return render(request, 'spese/tabellaSpese.html', {'spese':spese,'permessiAzioni': request.user.has_perm('gestioneMenu.delete_Spesa')})

@login_required
def effettuaSpese(request):
    if(request.method == 'POST'):
        spese = Spesa.objects.all()
        for spesa in spese:
            scorta = Scorta.objects.get(id = spesa.idScorta.id)
            scorta.quantitaAttuale = scorta.quantitaMinima
            scorta.save()
            aggiornaListe(scorta)
            return render(request, 'operazioneRiuscita.html', {'messaggio':"Lista della spesa svuotata!"})
    else:
        return Error

#Preparazioni
@login_required
def preparazioni(request):
    return render(request, 'preparazioni/preparazioni.html')

@login_required
def tabellaPreparazioni(request):
    preparazioni = Preparazione.objects.all()
    return render(request, 'preparazioni/tabellaPreparazioni.html', {'preparazioni':preparazioni, 'permessiAzioni': request.user.has_perm('gestioneMenu.delete_Preparazione') })


@login_required
def effettuaPreparazioni(request):
    if(request.method == 'POST'):
        preparazioni = Preparazione.objects.all()
        for preparazione in preparazioni:
            scorta = Scorta.objects.get(id = preparazione.idScorta)
            scorta.quantitaAttuale = scorta.quantitaMinima
            scorta.save()
            aggiornaListe(scorta)
            return render(request, 'operazioneRiuscita.html', {'messaggio':"Lista delle preparazioni svuotata!"})
    else:
        return Error

def aggiornaListe(scorta):
    print("Aggiorno.........")
    print(scorta.quantitaAttuale)
    print(scorta.quantitaMinima)
    if(scorta.quantitaAttuale < scorta.quantitaMinima):
        if(scorta.quantitaAttuale > 0 ):
            urgenza = 1
        else:
            urgenza = 2
 
        if(scorta.idIngrediente.fattoInCasa):
            try:
                preparazione = Preparazione.objects.get(idScorta = scorta)
            except Preparazione.DoesNotExist:
                preparazione = Preparazione(idScorta = scorta)
            preparazione.urgenza = urgenza
            preparazione.quantita = scorta.quantitaMinima - scorta.quantitaAttuale
            preparazione.save()
        else:
            try:
                spesa = Spesa.objects.get(idScorta = scorta)
            except Spesa.DoesNotExist:
                spesa = Spesa(idScorta = scorta)
            spesa.urgenza = urgenza
            spesa.quantita = scorta.quantitaMinima - scorta.quantitaAttuale
            spesa.save()
    else:
        if(scorta.idIngrediente.fattoInCasa):
            try:
                preparazione = Preparazione.objects.get(idScorta = scorta)
                preparazione.delete()
            except Preparazione.DoesNotExist:
                print("Preparazione inesistente")
        else:
            try:
                spesa = Spesa.objects.get(idScorta = scorta)
                spesa.delete()
            except Spesa.DoesNotExist:
                print("Spesa inesistente.")