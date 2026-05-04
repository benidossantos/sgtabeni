from django.db import models

class Tarefa(models.Model):
    STATUS_CHOICES = [
        ('ABERTA', 'Aberta'),
        ('CONCLUIDA', 'Concluída'),
    ]

    PRIORIDADE_CHOICES = [
        ('URGENTE', 'Urgente'),
        ('NAO_URGENTE', 'Não Urgente'),
    ]

    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ABERTA')
    prioridade = models.CharField(max_length=20, choices=PRIORIDADE_CHOICES, default='NAO_URGENTE')
    data_entrega = models.DateField()

    def __str__(self):
        return self.titulo
