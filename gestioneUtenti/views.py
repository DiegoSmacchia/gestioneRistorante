from django.contrib.auth import authenticate
from django.shortcuts import render
from django.contrib.auth import login, logout
from django.shortcuts import redirect
from django.contrib.auth.models import User
from gestioneUtenti.forms import UtenteForm
from django.contrib.auth.password_validation import validate_password, UserAttributeSimilarityValidator, MinimumLengthValidator, CommonPasswordValidator, NumericPasswordValidator
from django.core.exceptions import ValidationError

# Create your views here.
def paginaLogin(request):
    return render(request, "login.html")

def autenticazione(request):
    if request.method == 'POST':
        user = authenticate(username = request.POST['Username'], password = request.POST['Password'])
        print(user)
        if user is not None: 
            login(request, user)
            return redirect('home')
        else:
            return render(request, "loginErrore.html", {'messaggio': 'Credenziali non valide'})
    else:      
        return render(request, "loginErrore.html", {'messaggio': 'Richiesta non valida'})
    
def effettuaLogout(request):
    logout(request)
    return paginaLogin(request)

def registrazione(request):
    form = UtenteForm()
    return render(request, "registrazione.html", { 'form':form })

def nuovoUtente(request):
    if request.method == 'POST':
        form = UtenteForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            print(form.cleaned_data)
            # process the data in form.cleaned_data as required
            nuovoUtente = User(username = form.cleaned_data['username'],
                                password = form.cleaned_data['password'],
                                first_name = form.cleaned_data['nome'],
                                last_name = form.cleaned_data['cognome'],
                                email = form.cleaned_data['email'])
            try:
                validate_password(nuovoUtente.password, user=nuovoUtente, password_validators=[MinimumLengthValidator(8), UserAttributeSimilarityValidator(),CommonPasswordValidator(),NumericPasswordValidator()])
                newUtente = User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'], form.cleaned_data['password'])
                newUtente.save()
            except ValidationError as errori:
                erroreHTML = ""
                for errore in errori:
                    erroreHTML += errore + " "
                return render(request, "registrazioneErrore.html", { 'form':form, 'messaggio':erroreHTML })

            return redirect('home')
        else:
            return render(request, "registrazioneErrore.html", { 'form':form, 'messaggio':'valori inseriti non validi.' })
    else:
        form = UtenteForm()    
        return render(request, "registrazione.html", { 'form':form })

def confirmLogout(request):
    return render(request, 'contenutoDialogConfirm.html', {'titolo':'Conferma Logout', 'contenuto':'Vuoi Effettuare il Logout?', 'urlrichiesto':'effettuaLogout', 'hxtarget':'#contenutoTotale'})