# from django import forms
from django.forms import ModelForm 
from instrutor.models import Instrutor

# Create your models here.
# class InstrutorForm(forms.Form):    
    # rg = forms.CharField(max_length=15, null=False, help_text='Informe o RG do Instrutor')
    # nome = forms.CharField(max_length=70, null=False, help_text='Informe o nome do Instrutor')
    # dataNascimento = forms.DateField(null=False, help_text='Informe a data de nascimento do T[itulo')
    # ddd = forms.CharField(max_length=3, null=False, help_text='Informe o DDD do telefone do T[itulo')
    # telefone = forms.CharField(max_length=9, null=False, help_text='Informe o telefone do T[itulo')
    # titulo = forms.OneToOneField(Titulo, 
    #                              on_delete=models.CASCADE,
    #                              primary_key=True,
    # )

class InstrutorForm(ModelForm):
    
    class Meta:
        model = Instrutor
        fields = [ 'rg', 'nome', 'dataNascimento', 'ddd', 'telefone', 'titulo' ]
        
         
    
