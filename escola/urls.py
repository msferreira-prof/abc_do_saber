from django.urls import path
from escola import views


urlpatterns = [
    path('', views.escola, name='index'),
    path('abc/', views.abc123, name='abc123'),
]