from django.urls import path
from tipoatividade.views import inicio
from tipoatividade.views import fim

urlpatterns = [
    path('', inicio, name='inicio'),
    path('fim/', fim, name='fim'),
]