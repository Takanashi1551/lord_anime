from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.userView, name="user"),
    path('editar_user/<int:id>/', views.userEdit, name="editar_usuario"),
    path('eliminar_user/<int:id>/', views.userDelete, name="eliminar_usuario"),
    path('editar_pass/', views.userEditpass, name="editar_pass"),
    path('anime/', views.animesView, name="anime"),
    path('animes_add/', views.animesAdd, name="animes_add"),
    path('animes_edit/<int:id>/', views.animesEdit, name="animes_edit"),
    path('animes_delete/<int:id>/', views.animesDelete, name="animes_delete"),
    path('gender/', views.genderView, name="gender"),
    path('anime_chapter/', views.chapterAnimeView, name="anime_chapter"),
]