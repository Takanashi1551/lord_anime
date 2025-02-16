from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
def indexView(request):
    title = 'Hola angel'
    return render(request, 'index.html',{
        'title': title
    })

#@login_required
def loginView(request):
    return render(request, 'login.html')

def exit(request):
    logout(request)
    #podemos colocar el nombre index, pero uso el / para redireccionar
    return redirect('/')