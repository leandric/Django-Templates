from django.shortcuts import render
from usuarios.forms import LoginForms, CadastroForms


def login(request):
    form = LoginForms()

    return render(request, 'usuarios/login.html',{'form':form})

def cadastro(request):
    form = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)
    return render(request, 'usuarios/cadastro.html', {'form':form})
