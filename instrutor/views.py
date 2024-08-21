from django.shortcuts import render

# Create your views here.
def cadastrar(request):
    return render(request, 'instrutor/cadastroInstrutor.html')

def listar(request):
    return render(request, 'instrutor/listarInstrutores.html')

