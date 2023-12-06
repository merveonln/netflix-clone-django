from django.urls import path
from .views import *

urlpatterns = [
    path('register/', userRegister, name="register"),
    path('login/', userLogin, name="login"),
    path('logout/', userLogout, name="logout"),
    path('profiles/', profiles, name="profiles"),
    path('create/', createProfil, name="create"),
    path('hesap/', hesap, name="hesap"),
    path('delete/', userDelete, name="delete"),

]
