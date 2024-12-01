from django.shortcuts import render, redirect
from .forms import ManagerForm, loginManagerForm
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login
from django.contrib import messages


User = get_user_model

def index(request):
    return render(request, 'homePage/home.html')

def mainLogin(request):
    if request.user.is_authenticated:
        return redirect('homeManager:painelManager')
    else:
        if request.method == 'POST':
            form = loginManagerForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data  
                user = authenticate(request, username=cd['email'], password=cd['password'])
                print(user)
                if user is not None:
                    login(request, user)
                    print("tudo certo")
                    return redirect('homeManager:painelManager')
                else:
                    messages.error(request, "Email ou senha inválidos.")     
        else:
            form = loginManagerForm()
    return render(request, 'homePage/managerLogin.html', {'form': form})

def representanteLogin(request):
    return render(request, 'homePage/loginRepresentante.html')

def criar_formulario_manager(request):
    if request.method == 'POST':
        form = ManagerForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('managerLogin')
        else:
            return form.errors
    else:
        form = ManagerForm()
    return render(request, 'homePage/cadastro.html', {'form': form} )

