from django.core.checks.messages import Error
from django.shortcuts import render
from .models import Ingrediente, IngredientePiatto, Menu, Piatto
from django.contrib.auth.decorators import login_required
from .forms import IngredienteForm, IngredientePiattoForm, MenuForm, PiattoForm


# Create your views here.
def gestioneMenu(request):
    return render(request, 'gestioneMenu.html')

##Ingredienti
@login_required()
def ingredienti(request):
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
            nuovoIngrediente = Ingrediente(nome = form.cleaned_data['nome'], idMisura = form.cleaned_data['idMisura'], fattoInCasa = form.cleaned_data['fattoInCasa'])
            nuovoIngrediente.save()
            return render(request, 'operazioneRiuscita.html', {'messaggio':"Inserimento Riuscito!"})
        else:
            print(form)
            return render(request, 'operazioneFallita.html', {'messaggio':"Inserimento fallito, ricontrollare i campi!"})
    else:      
        return Error

@login_required()
def modificaIngrediente(request):
    if request.method == 'POST':
        idIngrediente = request.POST['idIngrediente']
        ingrediente = Ingrediente.objects.get(id=idIngrediente)
        form = IngredienteForm(initial={'nome':ingrediente.nome, 'idMisura':ingrediente.idMisura, 'fattoInCasa':ingrediente.fattoInCasa})

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
            ingrediente.idMisura = form.cleaned_data['idMisura']
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
    piattoform = PiattoForm()
    ingredientiPiatti = IngredientePiatto.objects.all()
    ingredientePiattoForm = IngredientePiattoForm()
    return render(request, 'piatti/piatti.html', {'piatti' : piatti, 'piattoform':piattoform, 
                                                'ingredientipiatti':ingredientiPiatti, 'ingredientepiattoform':ingredientePiattoForm,
                                                'permessiAzioni': request.user.has_perm('gestioneMenu.delete_IngredientePiatto')})

@login_required()
def nuovoPiatto(request):
    if request.method == 'POST':
        form = PiattoForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            nuovoPiatto = Piatto(nome = form.cleaned_data['nome'], 
                                idCategoria = form.cleaned_data['idCategoria'],
                                tempoPreparazione = form.cleaned_data['tempoPreparazione'],
                                tempoCottura = form.cleaned_data['tempoCottura'])
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

##IngredientiPiatti
@login_required()
def nuovoIngredientePiatto(request):
    if request.method == 'POST':
        form = IngredientePiattoForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            nuovoIngredientePiatto = IngredientePiatto()
            nuovoIngredientePiatto.idPiatto = form.cleaned_data['idPiatto']
            nuovoIngredientePiatto.idIngrediente = form.cleaned_data['idIngrediente']
            nuovoIngredientePiatto.quantita = form.cleaned_data['quantita']
            nuovoIngredientePiatto.save()
            return render(request, 'operazioneRiuscita.html', {'messaggio':"Inserimento Riuscito!"})
    else:      
        return Error

@login_required()
def modificaIngredientePiatto(request):
    if request.method == 'POST':
        idIngredientePiatto = request.POST['idIngredientePiatto']
        ingredientePiatto = IngredientePiatto.objects.get(id=idIngredientePiatto)
        form = IngredientePiattoForm(initial={'idPiatto':ingredientePiatto.idPiatto, 'idIngrediente':ingredientePiatto.idIngrediente, 'quantita':ingredientePiatto.quantita})

        return render(request, 'piatti/modificaIngredientePiatto.html', {'idIngredientePiatto':idIngredientePiatto, 'form':form})
    else:
        return Error

@login_required()
def applicaModificheIngredientePiatto(request):
    if request.method == 'POST':
        form = IngredientePiattoForm(request.POST)
        idIngredientePiatto = request.POST['idIngredientePiatto']
        if form.is_valid():
            ingredientePiatto = IngredientePiatto.objects.get(id=idIngredientePiatto)
            ingredientePiatto.idPiatto = form.cleaned_data['idPiatto']
            ingredientePiatto.idIngrediente = form.cleaned_data['idIngrediente']
            ingredientePiatto.quantita = form.cleaned_data['quantita']
            ingredientePiatto.save()
            return render(request, 'operazioneRiuscita.html', {'messaggio':"Modifica Riuscita!"})

    else:
        return Error
    
@login_required()
def eliminaIngredientePiatto(request):
    if request.method == 'POST':
        idIngredientePiatto = request.POST['idIngredientePiatto']
        ingredientePiatto = IngredientePiatto.objects.get(id=idIngredientePiatto)
        ingredientePiatto.delete()
        return render(request, 'operazioneRiuscita.html', {'messaggio':"Ingrediente del Piatto Eliminato!"})
    else:
        return Error

#Menu
@login_required()
def menu(request):
    piatti = Piatto.objects.all()
    piattiMenu = Menu.objects.all()
    piattiNonMenu = filtraPiattiNonMenu(piatti, piattiMenu)
    form = MenuForm()
    return render(request, 'menu/menu.html', {'menu' : piattiMenu, 'piattiNonMenu':piattiNonMenu, 'form':form, 'permessiAzioni': request.user.has_perm('gestioneMenu.delete_Menu')})

def filtraPiattiNonMenu(piatti, piattiMenu):
    piattiNonMenu = []
    idPiattiMenu = []
    for piatto in piattiMenu:
        idPiattiMenu.append(piatto.idPiatto.id)
    for piatto in piatti:
        if piatto.id not in idPiattiMenu:
            piattiNonMenu.append(piatto)
    return piattiNonMenu

@login_required()
def aggiungiPiattoMenu(request):
    if request.method == 'POST':
        idPiatto = request.POST['idPiatto']
        piatto = Piatto.objects.get(id = idPiatto)
        nomePiatto = piatto.nome
        form = MenuForm(initial={'idPiatto':piatto })
        print(form)
        return render(request, 'menu/aggiungiPiattoMenu.html', {'nomePiatto':nomePiatto, 'form':form})
    else:
        return Error

@login_required()
def applicaAggiuntaMenu(request):
    if request.method == 'POST':
        form = MenuForm(request.POST)
        if form.is_valid():
            menu = Menu()
            menu.idPiatto = form.cleaned_data['idPiatto']
            menu.descrizione = form.cleaned_data['descrizione']
            menu.prezzo = form.cleaned_data['prezzo']
            menu.save()
            return render(request, 'operazioneRiuscita.html', {'messaggio':"Aggiunta Riuscita!"})
        else:
            return render(request, 'operazioneFallita.html', {'messaggio':"Aggiunta Fallita, ricontrollare i campi!"})
    else:
        return Error
    
@login_required()
def eliminaPiattoMenu(request):
    if request.method == 'POST':
        idMenu = request.POST['idPiatto']
        menu = Menu.objects.get(id=idMenu)
        menu.delete()
        return render(request, 'operazioneRiuscita.html', {'messaggio':"Piatto Eliminato dal Menu!"})
    else:
        return Error
