# from django import forms
from django.forms import ModelForm
from tipoatividade.models import TipoAtividade

#class TipoAtividadeForm(forms.Form):
    # descricao = forms.CharField(max_length=70, required=True, help_text="Informe a descriçâo do Tipo de Atividade.")


class TipoAtividadeForm(ModelForm):
    class Meta:
        model = TipoAtividade
        fields = ['descricao']
    