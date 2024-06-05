from django.shortcuts import render
from .models import Topic
# Create your views here.


def index(request):
    '''A página inicial para o Registro de Aprendizagem'''
    return render(request, 'learning_logs/index.html')


def topics(request):
    """Mostra todos os tópicos"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)
