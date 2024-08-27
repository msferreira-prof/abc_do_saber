from django.db import models
from django.urls import reverse
from titulo.models import Titulo

# Create your models here.
class Instrutor(models.Model):
    """ Modelo representando um Instrutor """

    id = models.AutoField(primary_key=True, help_text="Id do Instrutor")
    rg = models.CharField(max_length=15, null=False, help_text='Informe o RG do Instrutor')
    nome = models.CharField(max_length=70, null=False, help_text='Informe o nome do Instrutor')
    dataNascimento = models.DateField(null=False, help_text='Informe a data de nascimento do T[itulo')
    ddd = models.CharField(max_length=3, null=False, help_text='Informe o DDD do telefone do T[itulo')
    telefone = models.CharField(max_length=9, null=False, help_text='Informe o telefone do T[itulo')
    titulo = models.ForeignKey(Titulo, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.id} - {self.nome} - {self.titulo.descricao}'
    
    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})
    
