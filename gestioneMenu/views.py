from django.core.checks.messages import Error
from django.shortcuts import render
from .models import Ingrediente, IngredientePiatto, Menu, Misura, Piatto, Categoria
from django.contrib.auth.decorators import login_required
from .forms import IngredienteForm, IngredientePiattoForm, MenuForm, MisuraForm, PiattoForm, CategoriaForm


# Create your views here.
@login_required
def gestioneMenu(request):
    return render(request, 'gestioneMenu.html', {'permessiAzioni':request.user.has_perm('gestioneMenu.delete_Ingrediente')})

##Ingredienti
@login_required()
def ingredienti(request):
    form = IngredienteForm()
    return render(request, 'ingredienti/ingredienti.html', {'form':form, 'permessiAzioni': request.user.has_perm('gestioneMenu.delete_Ingrediente') })

@login_required
def tabellaIngredienti(request):
    ingredienti = Ingrediente.objects.all()
    return render(request, 'ingredienti/tabellaIngredienti.html', {'ingredienti' : ingredienti,'permessiAzioni': request.user.has_perm('gestioneMenu.delete_Ingrediente')})

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
            return render(request, 'operazioneFallita.html', {'messaggio':"Modifica fallita, ricontrollare i campi!"})
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
    piattoform = PiattoForm()
    ingredientePiattoForm = IngredientePiattoForm()
    return render(request, 'piatti/piatti.html', {'piattoform':piattoform, 'ingredientepiattoform':ingredientePiattoForm,
                                                'permessiAzioni': request.user.has_perm('gestioneMenu.delete_IngredientePiatto')})

@login_required
def tabellaPiatti(request):
    piatti = Piatto.objects.all()
    return render(request, 'piatti/tabellaPiatti.html', {'piatti' : piatti, 'permessiAzioni': request.user.has_perm('gestioneMenu.delete_Piatto')})


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
        form = PiattoForm(initial={'nome':piatto.nome, 'tempoPreparazione':piatto.tempoPreparazione, 'tempoCottura':piatto.tempoCottura, 'idCategoria':piatto.idCategoria})

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
@login_required
def tabellaIngredientiPiatti(request):
    ingredientiPiatti = IngredientePiatto.objects.all()
    return render(request, 'piatti/tabellaIngredientiPiatti.html', {'ingredientipiatti':ingredientiPiatti, 'permessiAzioni': request.user.has_perm('gestioneMenu.delete_Ingrediente')})


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
    form = MenuForm()
    return render(request, 'menu/menu.html', {'form':form, 'permessiAzioni': request.user.has_perm('gestioneMenu.delete_Menu')})

@login_required()
def tabellaMenu(request):
    piattiMenu = Menu.objects.all()
    return render(request, 'menu/tabellaMenu.html', {'menu' : piattiMenu, 'permessiAzioni': request.user.has_perm('gestioneMenu.delete_Menu')})

@login_required()
def tabellaNonMenu(request):
    piatti = Piatto.objects.all()
    piattiMenu = Menu.objects.all()
    piattiNonMenu = filtraPiattiNonMenu(piatti, piattiMenu)
    print(piattiNonMenu)
    return render(request, 'menu/tabellaNonMenu.html', {'piattiNonMenu' : piattiNonMenu, 'permessiAzioni': request.user.has_perm('gestioneMenu.delete_Menu')})


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

##Misure
@login_required()
def misure(request):
    form = MisuraForm()
    return render(request, 'misure/misure.html', {'form':form, 'permessiAzioni': request.user.has_perm('gestioneMenu.delete_Misura') })

@login_required
def tabellaMisure(request):
    misure = Misura.objects.all()
    return render(request, 'misure/tabellaMisure.html', {'misure' : misure,'permessiAzioni': request.user.has_perm('gestioneMenu.delete_Misura')})

@login_required()
def nuovaMisura(request):
    if request.method == 'POST':
        form = MisuraForm(request.POST)
        if form.is_valid():
            nuovaMisura = Misura(nome = form.cleaned_data['nome'])
            nuovaMisura.save()
            return render(request, 'operazioneRiuscita.html', {'messaggio':"Inserimento Riuscito!"})
        else:
            return render(request, 'operazioneFallita.html', {'messaggio':"Inserimento fallito, ricontrollare i campi!"})
    else:      
        return Error

@login_required
def modificaMisura(request):
    if request.method == 'POST':
        idMisura = request.POST['idMisura']
        misura = Misura.objects.get(id=idMisura)
        form = MisuraForm(initial={'nome':misura.nome})

        return render(request, 'misure/modificaMisura.html', {'idMisura':idMisura, 'form':form})
    else:
        return Error

@login_required
def applicaModificheMisura(request):
    if request.method == 'POST':
        form = MisuraForm(request.POST)
        idMisura = request.POST['idMisura']
        if form.is_valid():
            misura = Misura.objects.get(id=idMisura)
            misura.nome = form.cleaned_data['nome']
            misura.save()

            return render(request, 'operazioneRiuscita.html', {'messaggio':"Modifica Riuscita!"})
        else:
            return render(request, 'operazioneFallita.html', {'messaggio':"Modifica fallita, ricontrollare i campi!"})
    else:
        return Error
    
@login_required()
def eliminaMisura(request):
    if request.method == 'POST':
        idMisura = request.POST['idMisura']
        misura = Misura.objects.get(id=idMisura)
        ingredienti = Ingrediente.objects.filter(idMisura = misura)
        if ingredienti.count() == 0:
            misura.delete()
            return render(request, 'operazioneRiuscita.html', {'messaggio':"Misura Eliminata!"})
        else:
            return render(request, 'operazioneFallita.html', {'messaggio':"Misura utilizzata in uno o più ingredienti!"})
    else:
        return Error

##Categorie
@login_required()
def categorie(request):
    form = CategoriaForm()
    return render(request, 'categorie/categorie.html', {'form':form, 'permessiAzioni': request.user.has_perm('gestioneMenu.delete_Categoria') })

@login_required
def tabellaCategorie(request):
    categorie = Categoria.objects.all()
    return render(request, 'categorie/tabellaCategorie.html', {'categorie' : categorie,'permessiAzioni': request.user.has_perm('gestioneMenu.delete_Categoria')})

@login_required()
def nuovaCategoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            nuovaCategoria = Categoria(nome = form.cleaned_data['nome'])
            nuovaCategoria.save()
            return render(request, 'operazioneRiuscita.html', {'messaggio':"Inserimento Riuscito!"})
        else:
            return render(request, 'operazioneFallita.html', {'messaggio':"Inserimento fallito, ricontrollare i campi!"})
    else:      
        return Error

@login_required
def modificaCategoria(request):
    if request.method == 'POST':
        idCategoria = request.POST['idCategoria']
        categoria = Categoria.objects.get(id=idCategoria)
        form = CategoriaForm(initial={'nome':categoria.nome})

        return render(request, 'categorie/modificaCategoria.html', {'idCategoria':idCategoria, 'form':form})
    else:
        return Error

@login_required
def applicaModificheCategoria(request):
    if request.method == 'POST':
        form = MisuraForm(request.POST)
        idCategoria = request.POST['idCategoria']
        if form.is_valid():
            categoria = Categoria.objects.get(id=idCategoria)
            categoria.nome = form.cleaned_data['nome']
            categoria.save()

            return render(request, 'operazioneRiuscita.html', {'messaggio':"Modifica Riuscita!"})
        else:
            return render(request, 'operazioneFallita.html', {'messaggio':"Modifica fallita, ricontrollare i campi!"})
    else:
        return Error
    
@login_required()
def eliminaCategoria(request):
    if request.method == 'POST':
        idCategoria = request.POST['idCategoria']
        categoria = Categoria.objects.get(id=idCategoria)
        piatti = Piatto.objects.filter(idCategoria = categoria)
        if piatti.count() == 0:
            categoria.delete()
            return render(request, 'operazioneRiuscita.html', {'messaggio':"Categoria Eliminata!"})
        else:
            return render(request, 'operazioneFallita.html', {'messaggio':"Categoria presente in uno o più piatti!"})
    else:
        return Error