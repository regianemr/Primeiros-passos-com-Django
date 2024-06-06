"""Define padrões de URL para pizzas_log"""

from django.urls import path

from . import views

app_name = 'pizzas_log'
urlpatterns = [
    # Página inicial
    path('', views.index, name='index'),
    # Página que mostra todos os ingredientes
    path('pizzas/', views.pizzas, name='pizzas'),
    # Página de detalhes para um único tópico
    path('pizzas/<int:pizza_id>/', views.pizza, name='pizza'),
]
