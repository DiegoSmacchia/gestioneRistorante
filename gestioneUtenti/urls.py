from django.urls import path
from . import views

urlpatterns = [
    path('', views.paginaLogin, name='login'),
    path('autenticazione', views.autenticazione, name='autenticazione'),
    path('logout', views.effettuaLogout, name='effettuaLogout'),
    path('registrazione', views.registrazione, name='registrazione'),
    path('nuovoUtente', views.nuovoUtente, name='nuovoUtente'),

    path('confirmLogout', views.confirmLogout, name='confirmLogout')
]