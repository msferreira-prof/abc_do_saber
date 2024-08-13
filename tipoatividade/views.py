from django.shortcuts import render
from django.http import HttpResponse
from tipoatividade.models import TipoAtividade

# Create your views here.
def inicio(request):
    return HttpResponse('<h3>Esta é a página de Tipo de Atividade</h3>')

def fim(request):
    return HttpResponse('acabou!')

def cadastrar(request):
    return render(request, 'tipoatividade/cadastroTiposAtividade.html')

def listar(request):
    # Busca todos os registros
    qtdTiposAtividade = TipoAtividade.objects.all().count()
    
    return render(request, 'tipoatividade/listarTiposAtividade.html')

