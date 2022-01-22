from django.urls import path
from . import views

urlpatterns = [
    path('', views.gestioneMagazzino, name='gestioneMagazzino'),
]