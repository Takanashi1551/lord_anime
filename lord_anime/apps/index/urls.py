from django.urls import path
from . import views
#from apps.index import views

urlpatterns = [
    path('', views.indexView, name="index"),
    path('login/', views.loginView, name="login"),
    path('register/', views.registerView, name="register"),
    path('admin-dashboard/', views.adminDashboard, name="admin_dashboard"),
    path('', views.userDashboard, name="user_dashboard"),
    path('reset-password', views.resetPasswordView, name="reset_password"),
    path('logout/', views.logoutView, name="exit"),
]