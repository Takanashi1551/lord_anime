from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.userView, name="user"),
    path('animes/', views.animeView, name="animes"),
    path('editar_user/<int:id>/', views.animeEdit, name="editar_usuario"),
]