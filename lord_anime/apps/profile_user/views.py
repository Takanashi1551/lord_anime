from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def profileView(request):
# Codigo para redireccionar al inicio si no esta logueado el usuario
    title = 'Bienvenido'
# Codigo para redireccionar al inicio si no esta logueado el usuario    
    if not request.user.is_authenticated:
        return redirect('index')
    return render(request, 'user/profile.html', {
        'title': title
    })