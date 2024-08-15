from django.shortcuts import render

# Create your views here.
def cadastrar(request):
    return render(request, 'aluno/cadastroAluno.html')

def listar(request):
    return render(request, 'aluno/listarAlunos.html')

