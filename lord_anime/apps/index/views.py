from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm

# Views of index
def indexView(request):
    title = 'Hola angel'
    return render(request, 'user/index.html',{
        'title': title
    })

# Views of login
def loginView(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.is_superuser:
                return redirect('admin_dashboard')
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html')      

# Views of admin dashboard
def adminDashboard(request):
    return render(request, 'admin/index.html')

# Views of users dashboard
@login_required
def userDashboard(request):
    return render(request, 'user/index.html')

# Views of Register
def registerView(request):
    data = {
        'form' : CustomUserCreationForm()
    }
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)
        if user_creation_form.is_valid():
            user_creation_form.save()
#una vez registrado, redireccionamos al login
            return redirect('/')
    return render(request, 'registration/register.html', data)

# Views of logout
def logoutView(request):
    logout(request)
    #podemos colocar el nombre index, pero uso el / para redireccionar
    return redirect('/')