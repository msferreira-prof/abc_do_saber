from django.shortcuts import render

# Create your views here.
def cadastrar(request):
    return render(request, 'titulo/cadastroTitulos.html')

def listar(request):
    return render(request, 'titulo/listarTitulos.html')

