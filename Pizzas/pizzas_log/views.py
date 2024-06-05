from django.shortcuts import render

# Create your views here.


def index(request):
    """A página inicial para o Registro de Aprendizagem"""
    return render(request, 'pizzas_log/index.html')
