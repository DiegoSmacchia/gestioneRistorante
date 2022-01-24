from django.urls import path
from . import views

urlpatterns = [
    path('', views.gestioneMenu, name='gestioneMenu'),
    path('ingredienti', views.ingredienti, name='ingredienti'),
    path('tabellaIngredienti', views.tabellaIngredienti, name='tabellaIngredienti'),
    path('nuovoIngrediente', views.nuovoIngrediente, name='nuovoIngrediente'),
    path('modificaIngrediente', views.modificaIngrediente, name='modificaIngrediente'),
    path('applicaInserimentoModificaIngrediente', views.applicaInserimentoModificaIngrediente, name='applicaInserimentoModificaIngrediente'),
    path('confirmEliminaIngrediente', views.confirmEliminaIngrediente, name='confirmEliminaIngrediente'),
    path('eliminaIngrediente', views.eliminaIngrediente, name='eliminaIngrediente'),

    path('piatti', views.piatti, name='piatti'),
    path('tabellaPiatti', views.tabellaPiatti, name='tabellaPiatti'),
    path('nuovoPiatto', views.nuovoPiatto, name='nuovoPiatto'),
    path('modificaPiatto', views.modificaPiatto, name='modificaPiatto'),
    path('applicaInserimentoModificaPiatto', views.applicaInserimentoModificaPiatto, name='applicaInserimentoModificaPiatto'),
    path('confirmEliminaPiatto', views.confirmEliminaPiatto, name='confirmEliminaPiatto'),
    path('eliminaPiatto', views.eliminaPiatto, name='eliminaPiatto'),

    path('tabellaIngredientiPiatti', views.tabellaIngredientiPiatti, name='tabellaIngredientiPiatti'),
    path('nuovoIngredientePiatto', views.nuovoIngredientePiatto, name='nuovoIngredientePiatto'),
    path('modificaIngredientePiatto', views.modificaIngredientePiatto, name='modificaIngredientePiatto'),
    path('applicaInserimentoModificaIngredientePiatto', views.applicaInserimentoModificaIngredientePiatto, name='applicaInserimentoModificaIngredientePiatto'),
    path('confirmEliminaIngredientePiatto', views.confirmEliminaIngredientePiatto, name='confirmEliminaIngredientePiatto'),
    path('eliminaIngredientePiatto', views.eliminaIngredientePiatto, name='eliminaIngredientePiatto'),

    path('menu', views.menu, name='menu'),
    path('tabellaMenu', views.tabellaMenu, name='tabellaMenu'),
    path('tabellaNonMenu', views.tabellaNonMenu, name='tabellaNonMenu'),
    path('aggiungiPiattoMenu', views.aggiungiPiattoMenu, name='aggiungiPiattoMenu'),
    path('applicaAggiuntaMenu', views.applicaAggiuntaMenu, name='applicaAggiuntaMenu'),
    path('confirmEliminaPiattoMenu', views.confirmEliminaPiattoMenu, name='confirmEliminaPiattoMenu'),
    path('eliminaPiattoMenu', views.eliminaPiattoMenu, name='eliminaPiattoMenu'),

    path('misure', views.misure, name='misure'),
    path('tabellaMisure', views.tabellaMisure, name='tabellaMisure'),
    path('nuovaMisura', views.nuovaMisura, name='nuovaMisura'),
    path('modificaMisura', views.modificaMisura, name='modificaMisura'),
    path('applicaInserimentoModificaMisura', views.applicaInserimentoModificaMisura, name='applicaInserimentoModificaMisura'),
    path('confirmEliminaMisura', views.confirmEliminaMisura, name='confirmEliminaMisura'),
    path('eliminaMisura', views.eliminaMisura, name='eliminaMisura'),

    path('categorie', views.categorie, name='categorie'),
    path('tabellaCategorie', views.tabellaCategorie, name='tabellaCategorie'),
    path('nuovaCategoria', views.nuovaCategoria, name='nuovaCategoria'),
    path('modificaCategoria', views.modificaCategoria, name='modificaCategoria'),
    path('applicaInserimentoModificaCategoria', views.applicaInserimentoModificaCategoria, name='applicaInserimentoModificaCategoria'),
    path('confirmEliminaCategoria', views.confirmEliminaCategoria, name='confirmEliminaCategoria'),
    path('eliminaCategoria', views.eliminaCategoria, name='eliminaCategoria'),
]