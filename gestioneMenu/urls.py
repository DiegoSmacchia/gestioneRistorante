from django.urls import path
from . import views

urlpatterns = [
    path('', views.gestioneMenu, name='gestioneMenu'),
    path('ingredienti', views.ingredienti, name='ingredienti'),
    path('nuovoIngrediente/', views.nuovoIngrediente, name='nuovoIngrediente'),
    path('modificaIngrediente/', views.modificaIngrediente, name='modificaIngrediente'),
    path('applicaModificheIngrediente', views.applicaModificheIngrediente, name='applicaModificheIngrediente'),
    path('eliminaIngrediente/', views.eliminaIngrediente, name='eliminaIngrediente'),
    path('piatti', views.piatti, name='piatti'),
    path('nuovoPiatto/', views.nuovoPiatto, name='nuovoPiatto'),
    path('modificaPiatto/', views.modificaPiatto, name='modificaPiatto'),
    path('applicaModifichePiatto', views.applicaModifichePiatto, name='applicaModifichePiatto'),
    path('eliminaPiatto/', views.eliminaPiatto, name='eliminaPiatto'),
    path('nuovoIngredientePiatto/', views.nuovoIngredientePiatto, name='nuovoIngredientePiatto'),
    path('modificaPiatto/', views.modificaPiatto, name='modificaPiatto'),
    path('applicaModifichePiatto', views.applicaModifichePiatto, name='applicaModifichePiatto'),
    path('eliminaPiatto/', views.eliminaPiatto, name='eliminaPiatto'),
]