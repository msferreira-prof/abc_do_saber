from django.shortcuts import render
from aluno.models import Aluno

# Create your views here.
def cadastrar(request):
    return render(request, 'aluno/cadastroAluno.html')

def listar(request):
    registros = Aluno.objects.all()
    
    contexto = {'alunos_lista': registros}
    
    return render(request, 'aluno/listarAlunos.html', contexto)
