from django.urls import path
from . import views
#from apps.index import views

urlpatterns = [
    path('', views.indexView, name="index"),
    path('login/', views.loginView, name="login"),
    path('logout/', views.exit, name="exit")
]