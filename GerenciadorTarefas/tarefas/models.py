from django.db import models
from django.contrib.auth import get_user_model

#classe que comporta os campos que vamos ter na tabela do sql
class Tarefa(models.Model):
    STATUS = (
        ('doing', 'Em andamento'),
        ('done', 'Concluída'),
        ('pending', 'Pendente')
    )
    
    titulo = models.CharField(max_length=50)
    descricao = models.TextField()
    done = models.CharField(
        max_length=7,
        choices=STATUS,        
    )   
    #se deletar usuário deleta tudo
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.titulo