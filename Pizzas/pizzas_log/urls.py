"""Define padrões de URL para pizzas_log"""

from django.urls import path

from . import views

app_name = 'pizzas_log'
urlpatterns = [
    # Página inicial
    path('', views.index, name='index'),
]
