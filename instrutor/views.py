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
    form = InstrutorForm(request.POST or None)
    if form.is_valid():
        # "salva em memoria", permitindo alterar o model instrutor 
        instrutor = form.save(commit=False)
        instrutor.save()

    form = InstrutorForm()

    registros = Titulo.objects.all()
    contexto = {'titulo_lista': registros}
    return render(request, 'instrutor/cadastroInstrutor.html', contexto)