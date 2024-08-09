from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<html><body><h2>Página de Resposta</h2><p>Olá, esta é a página de resposta</p></body></html>')

def abc123(request):
    return HttpResponse('abc 123')

def escola(request):
    return render(request, 'escola.html')

