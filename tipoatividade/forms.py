from django import forms

class TipoAtividadeForm(forms.Form):
    descricao = forms.CharField(max_length=70, required=True, help_text="Informe a descriçâo do Tipo de Atividade.")

    