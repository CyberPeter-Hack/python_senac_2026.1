from django.urls import path
from . import views

app_name = "loops" # Aula03

urlpatterns = [
    path('for/', views.pagina_for, name='pagina_for'),
    path('jogo/', views.jogo_adivinhacao, name='jogo_adivinhacao'),
    path('', views.index, name='index'), # Aula03
]