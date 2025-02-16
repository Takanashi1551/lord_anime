from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm

# Create your views here.
def indexView(request):
    title = 'Hola angel'
    return render(request, 'index.html',{
        'title': title
    })

#@login_required
def loginView(request):
    return render(request, 'registration/login.html')

def registerView(request):
    data = {
        'form' : CustomUserCreationForm()
    }
    
    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)
        if user_creation_form.is_valid():
            user_creation_form.save()
#una vez registrado, redireccionamos al login
            return redirect('/')
    return render(request, 'registration/register.html', data)

def exit(request):
    logout(request)
    #podemos colocar el nombre index, pero uso el / para redireccionar
    return redirect('/')