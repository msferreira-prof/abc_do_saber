from django.db import models
from django.urls import reverse

# Create your models here.
class Titulo(models.Model):
    
    """ Modelo representando um Titulo """
    
    codigo = models.AutoField(primary_key=True, null=False, help_text='Código do Tipo de atividade')
    descricao = models.CharField(max_length=70, null=False, help_text='Informe a descrição do Tipo de Atividade')
    
    def __str__(self):
        return f'{self.codigo} - {self.descricao}'
    
    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})
    