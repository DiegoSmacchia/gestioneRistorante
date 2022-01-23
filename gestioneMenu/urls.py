from django.urls import path
from . import views

urlpatterns = [
    path('', views.gestioneMenu, name='gestioneMenu'),
    path('ingredienti', views.ingredienti, name='ingredienti'),
    path('tabellaIngredienti', views.tabellaIngredienti, name='tabellaIngredienti'),
    path('nuovoIngrediente', views.nuovoIngrediente, name='nuovoIngrediente'),
    path('modificaIngrediente', views.modificaIngrediente, name='modificaIngrediente'),
    path('applicaModificheIngrediente', views.applicaModificheIngrediente, name='applicaModificheIngrediente'),
    path('eliminaIngrediente', views.eliminaIngrediente, name='eliminaIngrediente'),

    path('piatti', views.piatti, name='piatti'),
    path('tabellaPiatti', views.tabellaPiatti, name='tabellaPiatti'),
    path('nuovoPiatto', views.nuovoPiatto, name='nuovoPiatto'),
    path('modificaPiatto', views.modificaPiatto, name='modificaPiatto'),
    path('applicaModifichePiatto', views.applicaModifichePiatto, name='applicaModifichePiatto'),
    path('eliminaPiatto', views.eliminaPiatto, name='eliminaPiatto'),

    path('tabellaIngredientiPiatti', views.tabellaIngredientiPiatti, name='tabellaIngredientiPiatti'),
    path('nuovoIngredientePiatto', views.nuovoIngredientePiatto, name='nuovoIngredientePiatto'),
    path('modificaIngredientePiatto', views.modificaIngredientePiatto, name='modificaIngredientePiatto'),
    path('applicaModificheIngredientePiatto', views.applicaModificheIngredientePiatto, name='applicaModificheIngredientePiatto'),
    path('eliminaIngredientePiatto', views.eliminaIngredientePiatto, name='eliminaIngredientePiatto'),

    path('menu', views.menu, name='menu'),
    path('tabellaMenu', views.tabellaMenu, name='tabellaMenu'),
    path('tabellaNonMenu', views.tabellaNonMenu, name='tabellaNonMenu'),
    path('aggiungiPiattoMenu', views.aggiungiPiattoMenu, name='aggiungiPiattoMenu'),
    path('applicaAggiuntaMenu', views.applicaAggiuntaMenu, name='applicaAggiuntaMenu'),
    path('eliminaPiattoMenu', views.eliminaPiattoMenu, name='eliminaPiattoMenu'),

    path('misure', views.misure, name='misure'),
    path('tabellaMisure', views.tabellaMisure, name='tabellaMisure'),
    path('nuovaMisura', views.nuovaMisura, name='nuovaMisura'),
    path('modificaMisura', views.modificaMisura, name='modificaMisura'),
    path('applicaModificheMisura', views.applicaModificheMisura, name='applicaModificheMisura'),
    path('eliminaMisura', views.eliminaMisura, name='eliminaMisura'),

    path('categorie', views.categorie, name='categorie'),
    path('tabellaCategorie', views.tabellaCategorie, name='tabellaCategorie'),
    path('nuovaCategoria', views.nuovaCategoria, name='nuovaCategoria'),
    path('modificaCategoria', views.modificaCategoria, name='modificaCategoria'),
    path('applicaModificheCategoria', views.applicaModificheCategoria, name='applicaModificheCategoria'),
    path('eliminaCategoria', views.eliminaCategoria, name='eliminaCategoria'),
]