from django.core.checks.messages import Error
from django.shortcuts import render
from .models import Ingrediente, Piatto
from django.contrib.auth.decorators import login_required
from .forms import IngredienteForm, PiattoForm


# Create your views here.
def gestioneMenu(request):
    return render(request, 'gestioneMenu.html')

##Ingredienti
@login_required()
def ingredienti(request):
    print(request.user.has_perm('gestioneMenu.delete_Ingrediente'))
    ingredienti = Ingrediente.objects.all()
    form = IngredienteForm()
    return render(request, 'ingredienti/ingredienti.html', {'ingredienti' : ingredienti, 'form':form, 'permessiAzioni': request.user.has_perm('gestioneMenu.delete_Ingrediente')})

@login_required()
def nuovoIngrediente(request):
    if request.method == 'POST':
        form = IngredienteForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            nuovoIngrediente = Ingrediente(nome = form.cleaned_data['nome'], fattoInCasa = form.cleaned_data['fattoInCasa'])
            nuovoIngrediente.save()
            return render(request, 'operazioneRiuscita.html', {'messaggio':"Inserimento Riuscito!"})
        else:
            return render(request, 'operazioneFallita.html', {'messaggio':"Inserimento fallito, ricontrollare i campi!"})
    else:      
        return Error

@login_required()
def modificaIngrediente(request):
    if request.method == 'POST':
        idIngrediente = request.POST['idIngrediente']
        ingrediente = Ingrediente.objects.get(id=idIngrediente)
        form = IngredienteForm(initial={'nome':ingrediente.nome, 'fattoInCasa':ingrediente.fattoInCasa})

        return render(request, 'ingredienti/modificaIngrediente.html', {'idIngrediente':idIngrediente, 'form':form})
    else:
        return Error

@login_required()
def applicaModificheIngrediente(request):
    if request.method == 'POST':
        form = IngredienteForm(request.POST)
        idIngrediente = request.POST['idIngrediente']
        if form.is_valid():
            ingrediente = Ingrediente.objects.get(id=idIngrediente)
            ingrediente.nome = form.cleaned_data['nome']
            ingrediente.fattoInCasa = form.cleaned_data['fattoInCasa']
            ingrediente.save()
            return render(request, 'operazioneRiuscita.html', {'messaggio':"Modifica Riuscita!"})
        else:
            return render(request, 'operazioneFallita.html', {'messaggio':"Inserimento fallito, ricontrollare i campi!"})
    else:
        return Error
    
@login_required()
def eliminaIngrediente(request):
    if request.method == 'POST':
        idIngrediente = request.POST['idIngrediente']
        ingrediente = Ingrediente.objects.get(id=idIngrediente)
        ingrediente.delete()
        return render(request, 'operazioneRiuscita.html', {'messaggio':"Ingrediente Eliminato!"})
    else:
        return Error

##Piatti
@login_required()
def piatti(request):
    piatti = Piatto.objects.all()
    form = PiattoForm()
    return render(request, 'piatti/piatti.html', {'piatti' : piatti, 'form':form, 'permessiAzioni': request.user.has_perm('gestioneMenu.delete_Piatto')})

@login_required()
def nuovoPiatto(request):
    if request.method == 'POST':
        form = PiattoForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            nuovoPiatto = Piatto(nome = form.cleaned_data['nome'],  
                                tempoPreparazione = form.cleaned_data['tempoPreparazione'],
                                tempoCottura = form.cleaned_data['tempoCottura'])
            nuovoPiatto.tempoTotale = nuovoPiatto.tempoPreparazione + nuovoPiatto.tempoCottura
            nuovoPiatto.save()
            return render(request, 'operazioneRiuscita.html', {'messaggio':"Inserimento Riuscito!"})
    else:      
        return Error

@login_required()
def modificaPiatto(request):
    if request.method == 'POST':
        idPiatto = request.POST['idPiatto']
        piatto = Piatto.objects.get(id=idPiatto)
        form = PiattoForm(initial={'nome':piatto.nome, 'tempoPreparazione':piatto.tempoPreparazione, 'tempoCottura':piatto.tempoCottura})

        return render(request, 'piatti/modificaPiatto.html', {'idPiatto':idPiatto, 'form':form})
    else:
        return Error

@login_required()
def applicaModifichePiatto(request):
    if request.method == 'POST':
        form = PiattoForm(request.POST)
        idPiatto = request.POST['idPiatto']
        if form.is_valid():
            piatto = Piatto.objects.get(id=idPiatto)
            piatto.nome = form.cleaned_data['nome']
            piatto.tempoPreparazione = form.cleaned_data['tempoPreparazione']
            piatto.tempoCottura = form.cleaned_data['tempoCottura']
            piatto.tempoTotale = piatto.tempoPreparazione + piatto.tempoCottura
            piatto.save()
            return render(request, 'operazioneRiuscita.html', {'messaggio':"Modifica Riuscita!"})

    else:
        return Error
    
@login_required()
def eliminaPiatto(request):
    if request.method == 'POST':
        idPiatto = request.POST['idPiatto']
        piatto = Piatto.objects.get(id=idPiatto)
        piatto.delete()
        return render(request, 'operazioneRiuscita.html', {'messaggio':"Piatto Eliminato!"})
    else:
        return Error