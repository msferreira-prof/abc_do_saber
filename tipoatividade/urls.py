from django.urls import path
# from tipoatividade.views import inicio
# from tipoatividade.views import fim
from tipoatividade import views

urlpatterns = [
    # path('', inicio, name='inicio'),
    # path('fim/', fim, name='fim'),
    path('', views.cadastrar, name='cadastrar'),
    path('listar/', views.listar, name='listar')
]