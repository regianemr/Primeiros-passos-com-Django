from django.shortcuts import render, redirect

from .models import Topic
from .forms import TopicForm, EntryForm

# Create your views here.


def index(request):
    '''A página inicial para o Registro de Aprendizagem'''
    return render(request, 'learning_logs/index.html')


def topics(request):
    """Mostra todos os tópicos"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


def topic(request, topic_id):
    """Mostra um único tópico e todas as suas entradas"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


def new_topic(request):
    """Adiciona um tópico novo"""
    if request.method != 'POST':
        # Nenhum dado enviado; cria um formulário em branco.
        form = TopicForm()
    else:
        # Dadod POST enviados; processa os dados
        form = TopicForm(data=request.POST)

        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')

    # Exibe um formulário em branco ou inválido
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


def new_entry(request, topic_id):
    """Adiciona uma entrada nova para um tópico específico"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # Nenhum dado enviado; cria um formuário em branco
        form = EntryForm()
    else:
        # Dados POST enviados
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)

    # exibe um formulário em branco ou inválido
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)
