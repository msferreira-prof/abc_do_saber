from django.urls import path
from instrutor import views

urlpatterns = [
    path('', views.cadastrar, name='cadastrar_instrutor'),
    path('listar/', views.listar, name='listar_instrutor'),
]