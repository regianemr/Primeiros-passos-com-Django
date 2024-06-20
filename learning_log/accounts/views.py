from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def register(request):
    '''Cadastra um usuário novo'''
    if request.method != 'POST':
        # Exibe o formulário em branco de cadastro
        form = UserCreationForm()
    else:
        # Processa o formulário preechido
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # faz login do usuário e o redireciona para a página inicial
            login(request, new_user)
            return redirect('learning_logs:index')
    # exibe um formulário em branco ou inválido
    context = {'form': form}
    return render(request, 'registration/register.html', context)

# Create your views here.
