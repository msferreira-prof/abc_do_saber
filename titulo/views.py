from django.shortcuts import render
from titulo.models import Titulo
from titulo.forms import TituloForm
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def cadastrar(request):
    return render(request, 'titulo/cadastroTitulos.html')

def listar(request):
    registros = Titulo.objects.all()
    contexto = {'titulo_lista': registros}
    return render(request, 'titulo/listarTitulos.html', contexto)

@csrf_exempt
def cadastro(request):
    if request.method == 'POST':
        form = TituloForm(request.POST)
        if form.is_valid():
            dados_ta = form.cleaned_data
            titulo = Titulo(
                descricao = dados_ta['descricao']
            )
            titulo.save()
    
    return render(request, 'titulo/cadastroTitulos.html')

