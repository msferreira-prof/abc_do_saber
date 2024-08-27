from django.db import models
from django.urls import reverse

# Create your models here.
class Aluno(models.Model):
    
    """ Modelo representando um Aluno """
    
    matricula = models.AutoField(primary_key=True, null=False, help_text='Informe a matrícula do Aluno')
    nome = models.CharField(max_length=70, null=False, help_text='Informe o nome do Aluno')
    data_inicial = models.DateField(null=False, help_text='Informe a data de início de matrícula do Aluno')
    data_final = models.DateField(null=True, blank=True, help_text='Informe a data de fim de matrícula do Aluno')

    
    def __str__(self):
        return f'{self.matricula} - {self.nome}'
    
    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})
    