from django import forms
from .models.managers import Manager

class ManagerForm(forms.ModelForm):
    class Meta:
        model = Manager
        fields = ['name', 'email', 'password']
        error_messages = { 'nome': { 'required': "Por favor, insira o seu nome.", 'max_length': "O nome não pode ter mais de 255 caracteres.", }, 
                          'email': { 'required': "Por favor, insira o seu e-mail.", 'invalid': "Insira um e-mail válido.", }, 
                          'password': { 'required': "Por favor, insira a sua senha.", 'invalid': "Insira uma senha válida.", }, }
        
class loginManagerForm(forms.Form):
    email = forms.EmailField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    
    
