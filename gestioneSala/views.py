from aifc import Error
from datetime import datetime
from decimal import Decimal
from multiprocessing import Lock
from unicodedata import decimal
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ComponenteOrdineForm

from gestioneSala.forms import SalaForm, TavoloForm
from .models import ComponenteOrdine, ComponenteTemporaneo, Ordine, OrdineTemporaneo, Sala, Stato, Tavolo
from gestioneMenu.models import Piatto, Menu, IngredientePiatto
from gestioneMagazzino.views import massimoPiatti, aggiornaListe
from gestioneMagazzino.views import Scorta

# Create your views here.
@login_required
def gestioneSala(request):
    return render(request, 'gestioneSala.html', {'permessiAzioni': request.user.has_perm('gestioneMenu.delete_Ordine')})

@login_required
def saleTavoli(request):
    salaForm = SalaForm()
    tavoloForm = TavoloForm()
    return render(request, 'sale/sale.html', {'salaform' : salaForm, 'tavoloform' : tavoloForm,
                                            'permessiAzioni': request.user.has_perm('gestioneMenu.delete_Sala')})

@login_required()
def tabellaSale(request):
    sale = Sala.objects.all()
    return render(request, 'sale/tabellaSale.html', {'sale':sale, 'permessiAzioni': request.user.has_perm('gestioneMenu.delete_Sala')})

@login_required()
def tabellaTavoli(request):
    tavoli = Tavolo.objects.all().order_by('idSala')
    return render(request, 'sale/tabellaTavoli.html', {'tavoli':tavoli, 'permessiAzioni': request.user.has_perm('gestioneMenu.delete_Sala')})

## Sale
@login_required()
def nuovaSala(request):
    if request.method == 'POST':
        form = SalaForm()
        return render(request,  'sale/formSala.html', {'idSala':0, 'form':form, 'oggetto':'Inserimento'})
    else:      
        return Error

@login_required()
def modificaSala(request):
    if request.method == 'POST':
        idSala = request.POST['idSala']
        sala = Sala.objects.get(id=idSala)
        form = SalaForm(initial={'nome':sala.nome})

        return render(request, 'sale/formSala.html', {'idSala':idSala, 'form':form, 'oggetto':'Modifica'})
    else:
        return Error

@login_required()
def applicaInserimentoModificaSala(request):
    if request.method == 'POST':
        form = SalaForm(request.POST)
        idSala = request.POST['idSala']
        if form.is_valid():
            if idSala == '0':
                sala = Sala()
                if Sala.objects.filter(nome = form.cleaned_data['nome']):
                    return render(request, "operazioneFallita.html", {'messaggio':'Operazione fallita, sala gi?? presente!'})
            else:
                sala = Sala.objects.get(id=idSala)
            sala.nome = form.cleaned_data['nome']
            sala.save()
            return render(request, 'operazioneRiuscita.html', {'messaggio':"Operazione Riuscita!"})
        else:
            return render(request, 'operazioneFallita.html', {'messaggio':"Operazione Fallita, ricontrollare i campi!"})
    else:
        return Error
    
@login_required
def confirmEliminaSala(request):
    if request.method =='POST':
        return render(request, 'contenutoDialogConfirm.html', {'titolo':'Conferma Eliminazione', 
                                                            'contenuto':'Vuoi davvero eliminare questa sala?', 
                                                            'urlrichiesto':'eliminaSala', 
                                                            'hxtarget':'#divNotifica',
                                                            'parametro':request.POST['idSala'],
                                                            'nomeparametro':'idSala'})
    else:
        return Error

@login_required()
def eliminaSala(request):
    if request.method == 'POST':
        idSala = request.POST['idSala']
        sala = Sala.objects.get(id=idSala)
        tavoli = Tavolo.objects.filter(idSala = idSala)
        if not tavoli:
            sala.delete()
            return render(request, 'operazioneRiuscita.html', {'messaggio':"Sala Eliminata!"})
        else:
            return render(request, 'operazioneFallita.html', {'messaggio':"Eliminazione fallita: la sala contiene dei tavoli!"})
    else:
        return Error

##Tavoli
@login_required()
def nuovoTavolo(request):
    if request.method == 'POST':
        form = TavoloForm()
        return render(request, 'sale/formTavolo.html', {'idTavolo':0, 'form':form, 'oggetto':'Inserimento'})
    else:      
        return Error

@login_required()
def modificaTavolo(request):
    if request.method == 'POST':
        idTavolo = request.POST['idTavolo']
        tavolo = Tavolo.objects.get(id=idTavolo)
        form = TavoloForm(initial={'idSala':tavolo.idSala,'nome':tavolo.nome})

        return render(request, 'sale/formTavolo.html', {'idTavolo':idTavolo, 'form':form, 'oggetto':'Modifica'})
    else:
        return Error

@login_required()
def applicaInserimentoModificaTavolo(request):
    if request.method == 'POST':
        form = TavoloForm(request.POST)
        idTavolo = request.POST['idTavolo']
        if form.is_valid():
            if idTavolo == '0':
                tavolo = Tavolo()
                if Tavolo.objects.filter(nome = form.cleaned_data['nome'], idSala = form.cleaned_data['idSala']):
                    return render(request, "operazioneFallita.html", {'messaggio':'Operazione fallita, tavolo gi?? presente!'})
            else:
                tavolo = Tavolo.objects.get(id=idTavolo)
            tavolo.idSala = form.cleaned_data['idSala']
            tavolo.nome = form.cleaned_data['nome']
            tavolo.save()
            return render(request, 'operazioneRiuscita.html', {'messaggio':"Operazione Riuscita!"})
        else:
            return render(request, 'operazioneFallita.html', {'messaggio':"Operazione Fallita, ricontrollare i campi!"})
    else:
        return Error
    
@login_required
def confirmEliminaTavolo(request):
    if request.method =='POST':
        return render(request, 'contenutoDialogConfirm.html', {'titolo':'Conferma Eliminazione', 
                                                            'contenuto':'Vuoi davvero eliminare questo tavolo?', 
                                                            'urlrichiesto':'eliminaTavolo', 
                                                            'hxtarget':'#divNotificaTavolo',
                                                            'parametro':request.POST['idTavolo'],
                                                            'nomeparametro':'idTavolo'})
    else:
        return Error

@login_required()
def eliminaTavolo(request):
    if request.method == 'POST':
        idTavolo = request.POST['idTavolo']
        tavolo = Tavolo.objects.get(id=idTavolo)
        tavolo.delete()
        return render(request, 'operazioneRiuscita.html', {'messaggio':"Tavolo Eliminato!"})
    else:
        return Error

##Ordini
@login_required
def ordini(request):
    tavoliTotali = Tavolo.objects.all().order_by('idSala')
    ordini = Ordine.objects.all()
    tavoliOrdinato = []
    for ordine in ordini:
        tavoliOrdinato.append(ordine.idTavolo)
    return render(request, 'ordini/ordini.html', {'tavoli':tavoliTotali, 'ordini':ordini, 'tavoliordinato':tavoliOrdinato})

@login_required
def gestioneOrdine(request, idTavolo):
    if request.method == 'GET':

        piattiMenu = Menu.objects.all().order_by('idPiatto')
        try:
            ordine = Ordine.objects.get(idTavolo = idTavolo)
        except Ordine.DoesNotExist:
            ordine = None

        if ordine is not None:
            componenti = ComponenteOrdine.objects.filter(idOrdine = ordine.id)
        else:
            componenti = []
        try:
            ordineTemporaneo = OrdineTemporaneo.objects.get(idTavolo = idTavolo)
        except OrdineTemporaneo.DoesNotExist:
            ordineTemporaneo = OrdineTemporaneo()
        if ordineTemporaneo:
            componentiTemporanei = ComponenteTemporaneo.objects.filter(idOrdine = ordineTemporaneo).order_by('uscita')
        else:
            componentiTemporanei = []
        
        return render(request, "ordini/gestioneOrdine.html", {'ordine':ordine, 'componenti':componenti, 'componentitemporanei':componentiTemporanei,'piatti':piattiMenu, 'tavolo':idTavolo, 'idOrdineTemporaneo':ordineTemporaneo.id})
    else:
        return Error

@login_required
def tabellaOrdini(request, idTavolo):
        try:
            ordine = Ordine.objects.get(idTavolo = idTavolo)
        except Ordine.DoesNotExist:
            ordine = None

        if ordine is not None:
            componenti = ComponenteOrdine.objects.filter(idOrdine = ordine.id)
        else:
            componenti = []
        try:
            ordineTemporaneo = OrdineTemporaneo.objects.get(idTavolo = idTavolo)
        except OrdineTemporaneo.DoesNotExist:
            ordineTemporaneo = OrdineTemporaneo()
        if ordineTemporaneo:
            componentiTemporanei = ComponenteTemporaneo.objects.filter(idOrdine = ordineTemporaneo).order_by('uscita')
        else:
            componentiTemporanei = []
        return render(request, "ordini/tabellaOrdini.html", {'ordine':ordine, 'componenti':componenti,'componentitemporanei':componentiTemporanei, 'idOrdineTemporaneo':ordineTemporaneo.id, 'idTavolo':idTavolo})

@login_required
def aggiungiComponenteTemporaneo(request):
    if request.method == 'POST':
        idTavolo = request.POST['idTavolo']
        tavolo = Tavolo.objects.get(id = idTavolo)
        idPiatto = request.POST['idPiatto']
        piatto = Piatto.objects.get(id = idPiatto)
        uscita = request.POST['uscita']
        quantita = request.POST['quantita']
        variazioni = request.POST['variazioni']

        massimo = massimoPiatti(piatto.id)
        if float(quantita) <= massimo:
            try:
                ordineTemporaneo = OrdineTemporaneo.objects.get(idTavolo = idTavolo)
            except OrdineTemporaneo.DoesNotExist:
                ordineTemporaneo = None     
            if not ordineTemporaneo:
                ordineTemporaneo = OrdineTemporaneo(idTavolo = tavolo, orario=datetime.now().time())
                ordineTemporaneo.save()

            statoIniziale = Stato.objects.get(id = 1)
            componente = ComponenteTemporaneo(idOrdine = ordineTemporaneo, idPiatto = piatto, uscita = uscita, quantita = quantita, variazioni = variazioni, stato = statoIniziale)
            componente.save()
            return render(request, 'operazioneRiuscita.html', {'messaggio':'Inserimento del componente effettuato.'})
        else:
            messaggio = "Il massimo di " + piatto.nome + " ordinabile ?? " + str(massimo) + "."
            return render(request, 'operazioneFallita.html', {'messaggio':messaggio})

    else:
        return Error
    
@login_required
def confermaAggiuntaComponenti(request):
    if request.method == "POST":
        idOrdineTemporaneo = request.POST['idOrdineTemporaneo']
        ordineTemporaneo = OrdineTemporaneo.objects.get(id = idOrdineTemporaneo)
        componentiTemporanei = ComponenteTemporaneo.objects.filter(idOrdine = ordineTemporaneo).order_by('uscita')

        for componenteTemp in componentiTemporanei:
            massimo = massimoPiatti(componenteTemp.idPiatto.id)
            if float(componenteTemp.quantita) > massimo:
                messaggio = "Il massimo di " + componenteTemp.idPiatto.nome + " ordinabile ?? " + str(massimo) + "."
                return render(request, 'operazioneFallita.html', {'messaggio':messaggio})

        try:
            ordine = Ordine.objects.get(idTavolo = ordineTemporaneo.idTavolo)
        except Ordine.DoesNotExist:
            ordine = Ordine(idTavolo = ordineTemporaneo.idTavolo, orario=ordineTemporaneo.orario)
        ordine.save()
        for componenteTemp in componentiTemporanei:
            componente = ComponenteOrdine(idOrdine = ordine, 
                                        idPiatto = componenteTemp.idPiatto, 
                                        quantita = componenteTemp.quantita, 
                                        uscita = componenteTemp.uscita, 
                                        variazioni = componenteTemp.variazioni,
                                        stato = componenteTemp.stato)
            componente.save()

            ##Aggiornamento delle Scorte
            ingredientiPiatto = IngredientePiatto.objects.filter(idPiatto = componente.idPiatto)
            for ingrediente in ingredientiPiatto:
                try:
                    scorta = Scorta.objects.get(idIngrediente = ingrediente.idIngrediente)
                    scorta.quantitaAttuale -= float(Decimal(ingrediente.quantita) * componente.quantita)
                    scorta.save() 
                    aggiornaListe(scorta)
            
                except Scorta.DoesNotExist:
                    print("Scorta Inesistente.")

            componenteTemp.delete()
        ordineTemporaneo.delete()
        return render(request, 'operazioneRiuscita.html', {'messaggio':'ordine inserito!'})
    else:
        return Error

@login_required
def confirmEliminaComponenteTemporaneo(request):
    if request.method =='POST':
        return render(request, 'contenutoDialogConfirm.html', {'titolo':'Conferma Eliminazione', 
                                                            'contenuto':'Vuoi davvero eliminare questa parte di ordine?', 
                                                            'urlrichiesto':'eliminaComponenteTemporaneo', 
                                                            'hxtarget':'#divComponenteTemporaneo',
                                                            'parametro':request.POST['idComponente'],
                                                            'nomeparametro':'idComponente'})
    else:
        return Error

@login_required
def eliminaComponenteTemporaneo(request):
    if request.method == "POST":
        idComponente = request.POST['idComponente']
        componente = ComponenteTemporaneo.objects.get(id = idComponente)
        ordineTemporaneo = OrdineTemporaneo.objects.get(id = componente.idOrdine.id)

        componente.delete()
        componentiTemporanei = ComponenteTemporaneo.objects.filter(idOrdine = ordineTemporaneo).order_by('uscita')

        return render(request, 'ordini/ordiniTemporanei.html', {'componentitemporanei':componentiTemporanei, 'idOrdineTemporaneo':ordineTemporaneo.id})
    else:
        return Error

@login_required
def modificaComponenteOrdine(request):
    if request.method == 'POST':
        idComponente = request.POST['idComponente']
        componente = ComponenteOrdine.objects.get(id = idComponente)
        form = ComponenteOrdineForm(initial={'idPiatto':componente.idPiatto, 'quantita':componente.quantita,'uscita':componente.uscita,'variazioni':componente.variazioni })
        return render(request, 'ordini/modificaComponenteOrdine.html', {'idComponente':componente.id,'form':form})
    else:
        return Error

@login_required()
def applicaModificheComponenteOrdine(request):
    if request.method == 'POST':
        form = ComponenteOrdineForm(request.POST)
        idComponente = request.POST['idComponente']
        if form.is_valid():

            componente = ComponenteOrdine.objects.get(id=idComponente)
            ingredientiNuovoPiatto = IngredientePiatto.objects.filter(idPiatto = form.cleaned_data['idPiatto'])
            for ingrediente in ingredientiNuovoPiatto:
                    massimo = massimoPiatti(ingrediente.idPiatto.id)
            if float(form.cleaned_data['quantita']) > massimo:
                messaggio = "Il massimo di " + str(form.cleaned_data['idPiatto']) + " ordinabile ?? " + str(massimo) + "."
                return render(request, 'operazioneFallita.html', {'messaggio':messaggio})

            ##Aggiornamento delle Scorte
            if componente.idPiatto != form.cleaned_data['idPiatto']:

                ingredientiPiatto = IngredientePiatto.objects.filter(idPiatto = componente.idPiatto)
                for ingrediente in ingredientiPiatto:
                    try:
                        scorta = Scorta.objects.get(idIngrediente = ingrediente.idIngrediente)
                        scorta.quantitaAttuale += float(Decimal(ingrediente.quantita) * componente.quantita)
                        scorta.save() 
                        aggiornaListe(scorta)
            
                    except Scorta.DoesNotExist:
                        print("Scorta Inesistente.")
                
                ingredientiPiattoNuovo = IngredientePiatto.objects.filter(idPiatto = form.cleaned_data['idPiatto'])
                for ingrediente in ingredientiPiattoNuovo:
                    try:
                        scorta = Scorta.objects.get(idIngrediente = ingrediente.idIngrediente)
                        scorta.quantitaAttuale -= float(Decimal(ingrediente.quantita)) * float(form.cleaned_data['quantita'])
                        scorta.save() 
                        aggiornaListe(scorta)
            
                    except Scorta.DoesNotExist:
                        print("Scorta Inesistente.")
            else:
                if componente.quantita != form.cleaned_data['quantita']:
                    ingredientiPiatto = IngredientePiatto.objects.filter(idPiatto = componente.idPiatto)
                for ingrediente in ingredientiPiatto:
                    try:
                        scorta = Scorta.objects.get(idIngrediente = ingrediente.idIngrediente)
                        scorta.quantitaAttuale += float(Decimal(ingrediente.quantita) * componente.quantita)
                        scorta.quantitaAttuale -= float(ingrediente.quantita) * float(form.cleaned_data['quantita'])
                        scorta.save() 
                        aggiornaListe(scorta)
            
                    except Scorta.DoesNotExist:
                        print("Scorta Inesistente.")

            componente.idPiatto = form.cleaned_data['idPiatto']
            componente.quantita = form.cleaned_data['quantita']
            componente.uscita = form.cleaned_data['uscita']
            componente.variazioni = form.cleaned_data['variazioni']
            componente.save()
            return render(request, 'operazioneRiuscita.html', {'messaggio':"Modifica Riuscita!"})
        else:
            return render(request, 'operazioneFallita.html', {'messaggio':"Modifica fallita, ricontrollare i campi!"})
    else:
        return Error

 
@login_required
def confirmEliminaComponenteOrdine(request):
    if request.method =='POST':
        return render(request, 'contenutoDialogConfirm.html', {'titolo':'Conferma Eliminazione', 
                                                            'contenuto':'Vuoi davvero eliminare questa parte di ordine?', 
                                                            'urlrichiesto':'eliminaComponenteOrdine', 
                                                            'hxtarget':'#divModificaComponente',
                                                            'parametro':request.POST['idComponente'],
                                                            'nomeparametro':'idComponente'})
    else:
        return Error

@login_required()
def eliminaComponenteOrdine(request):
    if request.method == 'POST':
        idComponente = request.POST['idComponente']
        componente = ComponenteOrdine.objects.get(id=idComponente)

        ##Aggiornamento Scorte
        ingredientiPiatto = IngredientePiatto.objects.filter(idPiatto = componente.idPiatto)
        for ingrediente in ingredientiPiatto:
            try:
                scorta = Scorta.objects.get(idIngrediente = ingrediente.idIngrediente)
                scorta.quantitaAttuale += float(Decimal(ingrediente.quantita) * componente.quantita)
                scorta.save() 
                aggiornaListe(scorta)
            
            except Scorta.DoesNotExist:
                print("Scorta Inesistente.")

        componente.delete()
        return render(request, 'operazioneRiuscita.html', {'messaggio':"Componente Eliminato!"})
    else:
        return Error

@login_required
def conto(request, idTavolo):
    try:
        tavolo = Tavolo.objects.get(id = idTavolo)
        ordine = Ordine.objects.get(idTavolo = idTavolo)
        componentiOrdine = ComponenteOrdine.objects.filter(idOrdine = ordine)
        piattiMenu = Menu.objects.all()
        prezzoTotale = 0
        for componente in componentiOrdine:
            piatto = piattiMenu.get(idPiatto = componente.idPiatto)
            prezzo = Decimal(piatto.prezzo) * componente.quantita
            prezzoTotale += prezzo
        return render(request, "ordini/conto.html", {'componenti':componentiOrdine, 'totale':prezzoTotale, 'tavolo':tavolo})
    except Ordine.DoesNotExist:
        return Error

##Fine Servizio
@login_required
def confermaFineServizio(request):
    return render(request, 'contenutoDialogConfirm.html', {'titolo':'Conferma Fine Servizio', 
                                                        'contenuto':'Questa operazione canceller?? tutti gli ordini ricevuti, procedere?', 
                                                        'urlrichiesto':'fineServizio', 
                                                        'hxtarget':'#dialog',
                                                        'nonChiudereConferma':True})

def fineServizio(request):
    ordini = Ordine.objects.all()
    componenti = ComponenteOrdine.objects.all()
    ordiniTemp = OrdineTemporaneo.objects.all()
    componentiTemp = ComponenteTemporaneo.objects.all()

    for componente in componenti:
        if componente.stato != Stato.objects.get(id = 3):
            return render(request, 'contenutoAlert.html', {'titolo':'Errore', 'contenuto':'C\'?? almeno un ordine che non risulta concluso.',
                                                            'alertSuccesso':False, 'classetesto':'text-danger'})
    
    ordini.delete()
    componenti.delete()
    ordiniTemp.delete()
    componentiTemp.delete()
    return render(request, 'contenutoAlert.html', {'titolo':'Operazione Completata', 'contenuto':'Ordini chiusi!',
                                                            'alertSuccesso':True, 'classetesto':'text-success'})


