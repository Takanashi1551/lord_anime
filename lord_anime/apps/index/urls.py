from django.urls import path
from . import views
#from apps.index import views

urlpatterns = [
    path('', views.indexView, name="index"),
    path('login/', views.loginView, name="login"),
    path('register/', views.registerView, name="register"),
    path('logout/', views.exit, name="exit"),
]