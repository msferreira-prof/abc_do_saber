from django.urls import path
from contato import views

urlpatterns = [
    path('', views.registrar_contato, name='registrar_contato')
]
