from django.shortcuts import render, redirect, get_object_or_404
from apps.profile_user.models import users_photo
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from .forms import AnimeForm
from .models import animes, animes_genders

#Codigo para las acciones de la vista de boton usuario, editar y eliminar
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

def userEdit(request, id):
    if not request.user.is_superuser:
        return redirect('index')
    usuario = get_object_or_404(User, id=id)  # Buscar Anime por ID
    if request.method == 'POST':
        usuario.username = request.POST.get('username')
        usuario.email = request.POST.get('email')
        usuario.is_superuser = request.POST.get('is_superuser')
        usuario.is_active = request.POST.get('is_active')
        usuario.save()
        return redirect('user')
    return render(request, 'admin/user_edit.html', {'usuario': usuario})

def userEditpass(request):
    if not request.user.is_superuser:
        return redirect('index')
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password1 = request.POST.get('new_password1')
        new_password2 = request.POST.get('new_password2')

        if not old_password or not new_password1 or not new_password2:
            messages.error(request, 'Todos los campos son obligatorios.')
            return render(request, 'admin/user_editpass.html')
        if new_password1 != new_password2:
            messages.error(request, 'Las nuevas contraseñas no coinciden.')
            return render(request, 'admin/user_editpass.html')
        if not request.user.check_password(old_password):
            messages.error(request, 'La contraseña actual es incorrecta.')
            return render(request, 'admin/user_editpass.html')

        # Cambiar la contraseña
        request.user.set_password(new_password1)
        request.user.save()

        # Mantener la sesión activa después del cambio
        update_session_auth_hash(request, request.user)
        return redirect('index')
    return render(request, 'admin/user_editpass.html')

def userDelete(request, id):
    if not request.user.is_superuser:
        return redirect('index')
    usuario = get_object_or_404(User, id=id)
    usuario.delete()
    return redirect('user')

#Codigo para las acciones de la vista de boton poster, editar y eliminar
def animesView(request):
    if not request.user.is_superuser:
        return redirect('index')
    anime_list = animes.objects.all()
    return render(request, 'admin/anime_view.html', {'anime_list': anime_list})

def animesAdd(request):
    if not request.user.is_superuser:
        return redirect('index')
    if request.method == 'POST':
        animes_name = request.POST.get('animes_name')
        animes_sypnosis = request.POST.get('animes_sypnosis')
        animes_status = request.POST.get('animes_status')
        animes_type = request.POST.get('animes_type')
        animes_release_year = request.POST.get('animes_release_year')
        animes_poster_url = request.FILES.get('animes_poster_url')
        anime = animes(animes_name=animes_name, animes_sypnosis=animes_sypnosis, animes_status=animes_status, animes_type=animes_type, animes_release_year=animes_release_year, animes_poster_url=animes_poster_url)
        anime.save()
        return redirect('anime')
    return render(request, 'admin/anime_add.html')

def animesEdit(request, id):
    if not request.user.is_superuser:
        return redirect('index')
    anime = get_object_or_404(animes, id=id)
    if request.method == 'POST':
        anime.animes_name = request.POST.get('animes_name')
        anime.animes_sypnosis = request.POST.get('animes_sypnosis')
        anime.animes_status = request.POST.get('animes_status')
        anime.animes_type = request.POST.get('animes_type')
        anime.animes_release_year = request.POST.get('animes_release_year')
        anime.save()
        return redirect('anime')
    return render(request, 'admin/anime_edit.html', {'anime': anime})

def animesDelete(request, id):
    if not request.user.is_superuser:
        return redirect('index')
    anime = get_object_or_404(animes, id=id)
    anime.delete()
    return redirect('anime')

#Codigo para las acciones de la vista de boton generos, editar y eliminar
def genderView(request):
    if not request.user.is_superuser:
        return redirect('index')
    gender_list = animes_genders.objects.all()
    return render(request, 'admin/gender_view.html', {'gender_list': gender_list})


#Codigo para las acciones de la vista de boton animes, editar y eliminar
def chapterAnimeView(request):
    if not request.user.is_superuser:
        return redirect('index')
    return render(request, 'admin/chapter_anime.html')

