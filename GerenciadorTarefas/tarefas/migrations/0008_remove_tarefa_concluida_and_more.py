# Generated by Django 5.1.1 on 2024-09-10 03:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tarefas', '0007_tarefa_concluida_tarefa_data_de_entrega'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tarefa',
            name='concluida',
        ),
        migrations.RemoveField(
            model_name='tarefa',
            name='data_de_entrega',
        ),
    ]
