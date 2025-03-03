from django.urls import path
from . import views

urlpatterns = [
    path('mi-perfil/',views.profileView, name="profile"),
]