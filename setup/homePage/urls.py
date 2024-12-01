from django.urls import path, include
from homePage.views import *
from . import views



urlpatterns = [
    path('', index, name='home'),
    path('login/', mainLogin, name='managerLogin'),
    path('cadastroManager/', views.criar_formulario_manager, name='cadastrarManager'),
    path('loginRepresentante/', representanteLogin, name='loginRepresentante'),
]