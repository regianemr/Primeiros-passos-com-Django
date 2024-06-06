from django.shortcuts import render
from .models import Pizza
# Create your views here.


def index(request):
    """A página inicial para o Registro de Aprendizagem"""
    return render(request, 'pizzas_log/index.html')


def pizzas(request):
    """Mostra todas as pizzas"""
    pizzas = Pizza.objects.order_by('date_added')
    context = {'pizzas': pizzas}
    return render(request, 'pizzas_log/pizzas.html', context)


def pizza(request, pizza_id):
    """Mostra um único tópico"""
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.order_by('-date_added')
    context = {'pizza': pizza, 'toppings': toppings}
    return render(request, 'pizzas_log/pizza.html', context)
