from django.urls import path, include
from homeManager.views import *

app_name = 'homeManager'

urlpatterns = [
    path('painel/', home, name='painelManager'),
    path('logout/', include('homePage.urls'), name='managerLogout')
]