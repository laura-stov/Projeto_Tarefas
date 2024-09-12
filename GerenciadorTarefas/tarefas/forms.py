from django import forms
from .models import Tarefa
from django.contrib.auth import get_user_model

class TarefaFormulario(forms.ModelForm):

    class Meta:
        model = Tarefa
        fields = ['titulo', 'descricao', 'done']
        labels = {
            'titulo': 'Título',
            'descricao': 'Descrição',
            'done': 'Status'
        }