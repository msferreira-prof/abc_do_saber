from django.shortcuts import render
from instrutor.models import Instrutor
from instrutor.forms import InstrutorForm
from titulo.models import Titulo
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def cadastrar(request):
    titulos = Titulo.objects.all()
    contexto = {'titulo_lista': titulos}
    return render(request, 'instrutor/cadastroInstrutor.html', contexto)

def listar(request):
    registros = Instrutor.objects.all()
    contexto = {'instrutor_lista': registros}
    return render(request, 'instrutor/listarInstrutores.html', contexto)

@csrf_exempt
def cadastro(request):
    if request.method == 'POST':
        form = InstrutorForm(request.POST)
        if form.is_valid():
            dados_ta = form.cleaned_data
            instrutor = Instrutor(
                descricao = dados_ta['descricao']
            )
            instrutor.save()
    
    return render(request, 'instrutor/cadastroInstrutor.html')