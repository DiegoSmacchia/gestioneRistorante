from django.core.checks.messages import Error
from django.shortcuts import render
from .models import Ingrediente, IngredientePiatto, Menu, Misura, Piatto, Categoria
from django.contrib.auth.decorators import login_required
from .forms import IngredienteForm, IngredientePiattoForm, MenuForm, MisuraForm, PiattoForm, CategoriaForm


# Create your views here.
@login_required
def gestioneMenu(request):
    return render(request, 'gestioneMenu.html')

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
        form = IngredienteForm()
        return render(request, 'ingredienti/formIngrediente.html', {'idIngrediente':0, 'form':form, 'oggetto':'Inserimento'})
    else:
        return Error

@login_required()
def modificaIngrediente(request):
    if request.method == 'POST':
        idIngrediente = request.POST['idIngrediente']
        ingrediente = Ingrediente.objects.get(id=idIngrediente)
        form = IngredienteForm(initial={'nome':ingrediente.nome, 'idMisura':ingrediente.idMisura, 'fattoInCasa':ingrediente.fattoInCasa})

        return render(request, 'ingredienti/formIngrediente.html', {'idIngrediente':idIngrediente, 'form':form, 'oggetto':'Modifica'})
    else:
        return Error

@login_required
def applicaInserimentoModificaIngrediente(request):
    if request.method == 'POST':
        form = IngredienteForm(request.POST)
        idIngrediente = request.POST['idIngrediente']
        if form.is_valid():
            if idIngrediente == '0':
                ingrediente = Ingrediente()
                if Ingrediente.objects.filter(nome = form.cleaned_data['nome']):
                    return render(request, "operazioneFallita.html", {'messaggio':'Operazione fallita, ingrediente già presente!'})
            else:
                ingrediente = Ingrediente.objects.get(id=idIngrediente)

            ingrediente.nome = form.cleaned_data['nome']
            ingrediente.fattoInCasa = form.cleaned_data['fattoInCasa']
            ingrediente.idMisura = form.cleaned_data['idMisura']
            ingrediente.save()
            return render(request, 'operazioneRiuscita.html', {'messaggio':"Operazione Riuscita!"})
        else:
            return render(request, 'operazioneFallita.html', {'messaggio':"Operazione fallita, ricontrollare i campi!"})
    else:
        return Error
    
@login_required
def confirmEliminaIngrediente(request):
    if request.method =='POST':
        return render(request, 'contenutoDialogConfirm.html', {'titolo':'Conferma Eliminazione', 
                                                            'contenuto':'Vuoi davvero eliminare questo ingrediente?', 
                                                            'urlrichiesto':'eliminaIngrediente', 
                                                            'hxtarget':'#divNotifica',
                                                            'parametro':request.POST['idIngrediente'],
                                                            'nomeparametro':'idIngrediente'})
    else:
        return Error

@login_required
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
    piatti = Piatto.objects.all().order_by('idCategoria')
    return render(request, 'piatti/tabellaPiatti.html', {'piatti' : piatti, 'permessiAzioni': request.user.has_perm('gestioneMenu.delete_Piatto')})


@login_required()
def nuovoPiatto(request):
    if request.method == 'POST':
        form = PiattoForm()
        return render(request, 'piatti/formPiatto.html', {'idPiatto':0, 'form':form, 'oggetto':'Inserimento'})
    else:
        return Error

@login_required()
def modificaPiatto(request):
    if request.method == 'POST':
        idPiatto = request.POST['idPiatto']
        piatto = Piatto.objects.get(id=idPiatto)
        form = PiattoForm(initial={'nome':piatto.nome, 'idCategoria':piatto.idCategoria})

        return render(request, 'piatti/formPiatto.html', {'idPiatto':idPiatto, 'form':form, 'oggetto':'Modifica'})
    else:
        return Error

@login_required()
def applicaInserimentoModificaPiatto(request):
    if request.method == 'POST':
        form = PiattoForm(request.POST)
        idPiatto = request.POST['idPiatto']
        if form.is_valid():
            if idPiatto == '0':
                piatto = Piatto()
                if Piatto.objects.filter(nome = form.cleaned_data['nome']):
                    return render(request, "operazioneFallita.html", {'messaggio':'Operazione fallita, piatto già presente!'})
            else:
                piatto = Piatto.objects.get(id=idPiatto)
            piatto.idCategoria = form.cleaned_data['idCategoria']
            piatto.nome = form.cleaned_data['nome']
            piatto.save()
            return render(request, 'operazioneRiuscita.html', {'messaggio':"Operazione Riuscita!"})
        else:
            return render(request, "operazioneFallita.html", {'messaggio':'Operazione fallita, ricontrollare i campi!'})
    else:
        return Error
    
@login_required
def confirmEliminaPiatto(request):
    if request.method =='POST':
        return render(request, 'contenutoDialogConfirm.html', {'titolo':'Conferma Eliminazione', 
                                                            'contenuto':'Vuoi davvero eliminare questo piatto?', 
                                                            'urlrichiesto':'eliminaPiatto', 
                                                            'hxtarget':'#divNotifica',
                                                            'parametro':request.POST['idPiatto'],
                                                            'nomeparametro':'idPiatto'})
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
        form = IngredientePiattoForm()
        return render(request, 'piatti/formIngredientePiatto.html', {'idIngredientePiatto':0, 'form':form, 'oggetto':'Inserimento'})
    else:
        return Error

@login_required()
def modificaIngredientePiatto(request):
    if request.method == 'POST':
        idIngredientePiatto = request.POST['idIngredientePiatto']
        ingredientePiatto = IngredientePiatto.objects.get(id=idIngredientePiatto)
        form = IngredientePiattoForm(initial={'idPiatto':ingredientePiatto.idPiatto, 'idIngrediente':ingredientePiatto.idIngrediente, 'quantita':ingredientePiatto.quantita})

        return render(request, 'piatti/formIngredientePiatto.html', {'idIngredientePiatto':idIngredientePiatto, 'form':form, 'oggetto':'Modifica'})
    else:
        return Error

@login_required()
def applicaInserimentoModificaIngredientePiatto(request):
    if request.method == 'POST':
        form = IngredientePiattoForm(request.POST)
        idIngredientePiatto = request.POST['idIngredientePiatto']
        if form.is_valid():
            if idIngredientePiatto == '0':
                ingredientePiatto = IngredientePiatto()
                if IngredientePiatto.objects.filter(idPiatto = form.cleaned_data['idPiatto'], idIngrediente = form.cleaned_data['idIngrediente']):
                    return render(request, "operazioneFallita.html", {'messaggio':'Operazione fallita, ingrediente del piatto già presente!'})
            else:
                ingredientePiatto = IngredientePiatto.objects.get(id=idIngredientePiatto)
            ingredientePiatto.idPiatto = form.cleaned_data['idPiatto']
            ingredientePiatto.idIngrediente = form.cleaned_data['idIngrediente']
            ingredientePiatto.quantita = form.cleaned_data['quantita']
            ingredientePiatto.save()
            return render(request, 'operazioneRiuscita.html', {'messaggio':"Operazione Riuscita!"})
        else:
            return render(request, "operazioneFallita.html", {'messaggio':'Operazione fallita, ricontrollare i campi!'})
    else:
        return Error
    
@login_required
def confirmEliminaIngredientePiatto(request):
    if request.method =='POST':
        return render(request, 'contenutoDialogConfirm.html', {'titolo':'Conferma Eliminazione', 
                                                            'contenuto':'Vuoi davvero eliminare questo ingrediente del piatto?', 
                                                            'urlrichiesto':'eliminaIngredientePiatto', 
                                                            'hxtarget':'#divNotificaIngredientePiatto',
                                                            'parametro':request.POST['idIngredientePiatto'],
                                                            'nomeparametro':'idIngredientePiatto'})
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
    piattiMenu = Menu.objects.all().order_by('idPiatto')
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
    
@login_required
def confirmEliminaPiattoMenu(request):
    if request.method =='POST':
        return render(request, 'contenutoDialogConfirm.html', {'titolo':'Conferma Eliminazione', 
                                                            'contenuto':'Vuoi davvero eliminare questo piatto dal menu?', 
                                                            'urlrichiesto':'eliminaPiattoMenu', 
                                                            'hxtarget':'#divNotifica',
                                                            'parametro':request.POST['idPiatto'],
                                                            'nomeparametro':'idPiatto'})
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

@login_required
def nuovaMisura(request):
    if request.method == 'POST':
        form = MisuraForm()
        return render(request, 'misure/formMisura.html', {'idMisura':0, 'form':form, 'oggetto':'Inserimento'})
    else:
        return Error

@login_required
def modificaMisura(request):
    if request.method == 'POST':
        idMisura = request.POST['idMisura']
        misura = Misura.objects.get(id=idMisura)
        form = MisuraForm(initial={'nome':misura.nome})

        return render(request, 'misure/formMisura.html', {'idMisura':idMisura, 'form':form, 'oggetto':'Modifica'})
    else:
        return Error

@login_required
def applicaInserimentoModificaMisura(request):
    if request.method == 'POST':
        form = MisuraForm(request.POST)
        idMisura = request.POST['idMisura']
        if form.is_valid():
            print(idMisura)
            if idMisura == '0':
                misura = Misura()
                if Misura.objects.filter(nome = form.cleaned_data['nome']):
                    return render(request, "operazioneFallita.html", {'messaggio':'Operazione fallita, misura già presente!'})
            else:
                misura = Misura.objects.get(id=idMisura)
            misura.nome = form.cleaned_data['nome']
            misura.save()

            return render(request, 'operazioneRiuscita.html', {'messaggio':"Operazione Riuscita!"})
        else:
            return render(request, 'operazioneFallita.html', {'messaggio':"Operazione fallita, ricontrollare i campi!"})
    else:
        return Error
    
@login_required
def confirmEliminaMisura(request):
    if request.method =='POST':
        return render(request, 'contenutoDialogConfirm.html', {'titolo':'Conferma Eliminazione', 
                                                            'contenuto':'Vuoi davvero eliminare questa misura?', 
                                                            'urlrichiesto':'eliminaMisura', 
                                                            'hxtarget':'#divNotifica',
                                                            'parametro':request.POST['idMisura'],
                                                            'nomeparametro':'idMisura'})
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

@login_required
def nuovaCategoria(request):
    if request.method == 'POST':
        form = CategoriaForm()
        return render(request, 'categorie/formCategoria.html', {'idCategoria':0, 'form':form, 'oggetto':'Inserimento'})
    else:
        return Error

@login_required
def modificaCategoria(request):
    if request.method == 'POST':
        idCategoria = request.POST['idCategoria']
        categoria = Categoria.objects.get(id=idCategoria)
        form = CategoriaForm(initial={'nome':categoria.nome})

        return render(request, 'categorie/formCategoria.html', {'idCategoria':idCategoria, 'form':form, 'oggetto':'Modifica'})
    else:
        return Error

@login_required
def applicaInserimentoModificaCategoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        idCategoria = request.POST['idCategoria']
        if form.is_valid():
            if idCategoria == '0':
                categoria = Categoria()
                if Categoria.objects.filter(nome = form.cleaned_data['nome']):
                    return render(request, "operazioneFallita.html", {'messaggio':'Operazione fallita, categoria già presente!'})
            else:
                categoria = Categoria.objects.get(id=idCategoria)
            categoria.nome = form.cleaned_data['nome']
            categoria.save()

            return render(request, 'operazioneRiuscita.html', {'messaggio':"Operazione Riuscita!"})
        else:
            return render(request, 'operazioneFallita.html', {'messaggio':"Operazione fallita, ricontrollare i campi!"})
    else:
        return Error

@login_required
def confirmEliminaCategoria(request):
    if request.method =='POST':
        return render(request, 'contenutoDialogConfirm.html', {'titolo':'Conferma Eliminazione', 
                                                            'contenuto':'Vuoi davvero eliminare questa categoria?', 
                                                            'urlrichiesto':'eliminaCategoria', 
                                                            'hxtarget':'#divNotifica',
                                                            'parametro':request.POST['idCategoria'],
                                                            'nomeparametro':'idCategoria'})
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