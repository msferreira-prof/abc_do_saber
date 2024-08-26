from django.shortcuts import render
from django.http import HttpResponse
from tipoatividade.models import TipoAtividade
from tipoatividade.forms import TipoAtividadeForm
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def inicio(request):
    return HttpResponse('<h3>Esta é a página de Tipo de Atividade</h3>')

def fim(request):
    return HttpResponse('acabou!')

def cadastrar(request):
    return render(request, 'tipoatividade/cadastroTiposAtividade.html')

def listar(request):
    registros = TipoAtividade.objects.all()
    contexto = {'tipos_atividade_lista': registros}

    return render(request, 'tipoatividade/listarTiposAtividade.html', contexto)

@csrf_exempt
def cadastro(request):
    if request.method == 'POST':
        form = TipoAtividadeForm(request.POST)
        if form.is_valid():
            dados_ta = form.cleaned_data
            tipo_atividade = TipoAtividade(
                descricao = dados_ta['descricao']
            )
            tipo_atividade.save()
    
    return render(request, 'tipoatividade/cadastroTiposAtividade.html')

