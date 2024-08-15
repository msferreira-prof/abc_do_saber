from django.urls import path
from aluno import views

urlpatterns = [
    path('', views.cadastrar, name='cadastrar_aluno'),
    path('listar/', views.listar, name='listar_aluno'),
]