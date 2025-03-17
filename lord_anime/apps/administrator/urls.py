from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.userView, name="user"),
    path('animes/', views.animeView, name="animes"),
    path('editar_user/<int:id>/', views.userEdit, name="editar_usuario"),
    path('eliminar_user/<int:id>/', views.userDelete, name="eliminar_usuario"),
    path('editar_pass/', views.userEditpass, name="editar_pass"),
]