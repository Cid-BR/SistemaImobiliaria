from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from SistemaImobiliaria.contas.forms import LoginForm
from django.shortcuts import redirect


def user_login(request):
    
    if request.user.is_authenticated:
        return render(request, 'imobiliaria/index.html')

    if request.method == 'POST':
    
        form = LoginForm(request.POST)
        context = {'voltar':'/'} 

        if form.is_valid():
            cd = form.cleaned_data
#            verification of the user
            try:
                user = User.objects.get(username=cd['username'])
            except:
                context.update({'erro':'Usuário não encontrado'})
                return render(request, 'error.html', context)
#            verification of the password
            if user is not None and user.check_password(cd['password']):
                if user.is_active:
                    login(request, user)
                    return render(request, 'imobiliaria/index.html')
                else:
                    context.update({'erro':'Usuário inativo'})
                    return render(request, 'error.html', context)
            else:
                context.update({'erro':'Senha inválida'})
                return render(request, 'error.html', context)
    
    else:
        form = LoginForm()
    
    return render(request, 'contas/index.html', {'form': form})
    
    
def user_logout(request):
    logout(request)
    return render(request, 'index.html')    
