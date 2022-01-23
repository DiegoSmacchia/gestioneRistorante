from django.urls import path
from . import views

urlpatterns = [
    path('', views.gestioneMagazzino, name='gestioneMagazzino'),
    path('scorte', views.scorte, name='scorte'),
    path('tabellaScorte', views.tabellaScorte, name='tabellaScorte'),
    path('nuovaScorta', views.nuovaScorta, name='nuovaScorta'),
    path('modificaScorta', views.modificaScorta, name='modificaScorta'),
    path('applicaModificheScorta', views.applicaModificheScorta, name='applicaModificheScorta'),
    path('eliminaScorta', views.eliminaScorta, name='eliminaScorta'),
    path('spese', views.spese, name='spese'),
    path('tabellaSpese', views.tabellaSpese, name='tabellaSpese'),
    path('effettuaSpese', views.effettuaSpese, name='effettuaSpese'),
    path('preparazioni', views.preparazioni, name='preparazioni'),
    path('tabellaPreparazioni', views.tabellaPreparazioni, name='tabellaPreparazioni'),
    path('effettuaPreparazioni', views.effettuaPreparazioni, name='effettuaPreparazioni'),
    
]