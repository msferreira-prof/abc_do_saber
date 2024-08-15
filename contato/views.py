from django.shortcuts import render

# Create your views here.
def registrar_contato(request):
    return render(request, 'contato/contato.html')

