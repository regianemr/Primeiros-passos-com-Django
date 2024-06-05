from django.urls import path

from . import views

app_name = 'meal_plans'
urlpatterns = [
    # Página inicial
    path('', views.index, name='index'),
]
