from django.urls import path
from . import views

urlpatterns = [
    path('', views.gestioneSala, name='gestioneSala'),
    path('sale', views.saleTavoli, name = 'saleTavoli'),
    path('tabellaSale', views.tabellaSale, name='tabellaSale'),
    path('tabellaTavoli', views.tabellaTavoli, name='tabellaTavoli'),
    path('nuovaSala', views.nuovaSala, name='nuovaSala'),
    path('modificaSala', views.modificaSala, name='modificaSala'),
    path('applicaModificheSala', views.applicaModificheSala, name='applicaModificheSala'),
    path('eliminaSala', views.eliminaSala, name='eliminaSala'),
    path('nuovoTavolo', views.nuovoTavolo, name='nuovoTavolo'),
    path('modificaTavolo', views.modificaTavolo, name='modificaTavolo'),
    path('applicaModificheTavolo', views.applicaModificheTavolo, name='applicaModificheTavolo'),
    path('eliminaTavolo/', views.eliminaTavolo, name='eliminaTavolo'),
    path('ordini', views.ordini, name = 'ordini'),
    path('gestioneOrdine/<int:idTavolo>', views.gestioneOrdine, name = 'gestioneOrdine'),
    path('tabellaOrdini/<int:idTavolo>', views.tabellaOrdini, name='tabellaOrdini'),
    path('aggiungiComponenteTemporaneo', views.aggiungiComponenteTemporaneo, name='aggiungiComponenteTemporaneo'),
    path('confermaAggiuntaComponenti', views.confermaAggiuntaComponenti, name ='confermaAggiuntaComponenti'),
    path('eliminaComponenteTemporaneo', views.eliminaComponenteTemporaneo, name ='eliminaComponenteTemporaneo'),
    path('modificaComponenteOrdine', views.modificaComponenteOrdine, name='modificaComponenteOrdine'),
    path('applicaModificheComponenteOrdine', views.applicaModificheComponenteOrdine, name='applicaModificheComponenteOrdine'),
    path('eliminaComponenteOrdine', views.eliminaComponenteOrdine, name='eliminaComponenteOrdine'),

]