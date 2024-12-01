from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def managerLogout(request):
        logout(request)
        return redirect('homePage:home')
    
@login_required
def home(request):
        name = request.user.name
        print("teste")
        context = {
            'nome': name
        }
        return render(request, 'homeManager/home.html', context)

