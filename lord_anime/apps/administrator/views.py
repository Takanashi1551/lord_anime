from django.shortcuts import render, redirect, get_object_or_404
from apps.profile_user.models import users_photo
from django.contrib.auth.models import User
from .forms import UserEditForm

# Create your views here.
def userView(request):
# Codigo para redireccionar al inicio si no es superusuario
    if not request.user.is_superuser:
# Codigo para redireccionar si no estamos logueados
        if not request.user.is_authenticated:
            return redirect('index')
        return redirect('index')
    usuarios = User.objects.all()
    animes = users_photo.objects.select_related('fk_users_aut_user').all()
    return render(request, 'admin/user.html',{'usuarios': usuarios, 'animes': animes})

def animeView(request):
    if not request.user.is_superuser:
        return redirect('index')
    return render(request, 'admin/animes.html')

def animeEdit(request, id):
    if not request.user.is_superuser:
        return redirect('index')
    usuario = get_object_or_404(User, id=id)  # Buscar Anime por ID
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=usuario)  # Form con datos nuevos
        if form.is_valid():
            form.save()  # Guardar cambios
            return redirect('user')  # Redirigir a la lista o detalle
    else:
        form = UserEditForm(instance=usuario)  # Form con datos actuales
    return render(request, 'admin/user_edit.html', {'form': form})