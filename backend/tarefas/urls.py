from django.urls import path
from .views import *

urlpatterns = [
    path('tarefas/', listar_tarefas),
    path('tarefas/prioridade/<str:prioridade>/', tarefas_por_prioridade),
    path('tarefas/<int:id>/', tarefa_por_id),
    path('tarefas/urgentes-abertas/', tarefas_urgentes_abertas),
    path('tarefas/atrasadas/', tarefas_atrasadas),
    path('tarefas/busca/<str:palavra>/', buscar_tarefas),
]