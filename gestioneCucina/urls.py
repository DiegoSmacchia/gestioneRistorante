from django.urls import path
from . import views

urlpatterns = [
    path('', views.gestioneCucina, name='gestioneCucina'),
    path('contenutoCucina', views.contenutoCucina, name='contenutoCucina'),
    path('componenteServito', views.componenteServito, name='componenteServito'),
    path('inizioPreparazioneComponente', views.inizioPreparazioneComponente, name='inizioPreparazioneComponente'),
    path('alagi', views.alagi, name='alagi')
]