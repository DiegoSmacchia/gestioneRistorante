from django import forms
from django.contrib.auth.password_validation import UserAttributeSimilarityValidator, MinimumLengthValidator, CommonPasswordValidator, NumericPasswordValidator

class UtenteForm(forms.Form):
    username = forms.CharField(label='Username:', max_length=100)
    nome = forms.CharField(label= "Nome:", max_length=100, required=False)
    cognome = forms.CharField(label="Cognome:",max_length=100, required=False)
    password = forms.CharField(label= "Password:", max_length=100, widget=forms.PasswordInput())
    email = forms.EmailField(label="Email:", required=False)
    

