from django.shortcuts import render

def index(request):
    return render(request, 'homePage/home.html')

def mainLogin(request):
    return render(request, 'homePage/managerLogin.html')

def mainCadastro(request):
    return render(request, 'homePage/cadastro.html')

def representanteLogin(request):
    return render(request, 'homePage/loginRepresentante.html')
