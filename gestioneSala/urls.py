from django.urls import path
from . import views

urlpatterns = [
    path('', views.gestioneSala, name='gestioneSala'),
    path('sale', views.saleTavoli, name = 'saleTavoli'),
    path('tabellaSale', views.tabellaSale, name='tabellaSale'),
    path('tabellaTavoli', views.tabellaTavoli, name='tabellaTavoli'),

    path('nuovaSala', views.nuovaSala, name='nuovaSala'),
    path('modificaSala', views.modificaSala, name='modificaSala'),
    path('applicaInserimentoModificaSala', views.applicaInserimentoModificaSala, name='applicaInserimentoModificaSala'),
    path('confiemEliminaSala', views.confirmEliminaSala, name='confirmEliminaSala'),
    path('eliminaSala', views.eliminaSala, name='eliminaSala'),

    path('nuovoTavolo', views.nuovoTavolo, name='nuovoTavolo'),
    path('modificaTavolo', views.modificaTavolo, name='modificaTavolo'),
    path('applicaInserimentoModificaTavolo', views.applicaInserimentoModificaTavolo, name='applicaInserimentoModificaTavolo'),
    path('confirmEliminaTavolo', views.confirmEliminaTavolo, name='confirmEliminaTavolo'),
    path('eliminaTavolo/', views.eliminaTavolo, name='eliminaTavolo'),

    path('ordini', views.ordini, name = 'ordini'),
    path('gestioneOrdine/<int:idTavolo>', views.gestioneOrdine, name = 'gestioneOrdine'),
    path('tabellaOrdini/<int:idTavolo>', views.tabellaOrdini, name='tabellaOrdini'),
    path('aggiungiComponenteTemporaneo', views.aggiungiComponenteTemporaneo, name='aggiungiComponenteTemporaneo'),
    path('confermaAggiuntaComponenti', views.confermaAggiuntaComponenti, name ='confermaAggiuntaComponenti'),
    path('confirmEliminaComponenteTemporaneo', views.confirmEliminaComponenteTemporaneo, name='confirmEliminaComponenteTemporaneo'),
    path('eliminaComponenteTemporaneo', views.eliminaComponenteTemporaneo, name ='eliminaComponenteTemporaneo'),

    path('modificaComponenteOrdine', views.modificaComponenteOrdine, name='modificaComponenteOrdine'),
    path('applicaModificheComponenteOrdine', views.applicaModificheComponenteOrdine, name='applicaModificheComponenteOrdine'),
    path('confirmEliminaComponenteOrdine', views.confirmEliminaComponenteOrdine, name='confirmEliminaComponenteOrdine'),
    path('eliminaComponenteOrdine', views.eliminaComponenteOrdine, name='eliminaComponenteOrdine'),

    path('conto/<int:idTavolo>', views.conto, name = 'conto'),

    path('confermaFineServizio', views.confermaFineServizio, name='confermaFineServizio'),
    path('fineServizio', views.fineServizio, name='fineServizio')

]