from django.urls import path
from homePage.views import index, mainLogin, mainCadastro, representanteLogin

urlpatterns = [
    path('', index, name='home'),
    path('login/', mainLogin, name='managerLogin'),
    path('cadastroManager/', mainCadastro, name='cadastrarManager'),
    path('loginRepresentante/', representanteLogin, name='loginRepresentante'),
]