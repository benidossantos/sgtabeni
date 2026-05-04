from django.http import JsonResponse
from .models import Tarefa
from datetime import date

# Listar todas
def listar_tarefas(request):
    tarefas = Tarefa.objects.all()

    lista = []
    for t in tarefas:
        lista.append({
            "id": t.id,
            "titulo": t.titulo,
            "descricao": t.descricao,
            "status": t.status,
            "prioridade": t.prioridade,
            "usuario_responsavel": t.usuario_responsavel.nome if t.usuario_responsavel else None
        })

    return JsonResponse(lista, safe=False)

# EX 2 - por prioridade
def tarefas_por_prioridade(request, prioridade):
    tarefas = Tarefa.objects.filter(prioridade=prioridade).values()
    return JsonResponse(list(tarefas), safe=False)

# EX 3 - por ID
def tarefa_por_id(request, id):
    try:
        tarefa = Tarefa.objects.get(id=id)
        return JsonResponse({
            "id": tarefa.id,
            "titulo": tarefa.titulo,
            "descricao": tarefa.descricao,
            "status": tarefa.status,
            "prioridade": tarefa.prioridade
        })
    except Tarefa.DoesNotExist:
        return JsonResponse({"erro": "Tarefa não encontrada"})

# EX 4 - abertas e urgentes
def tarefas_urgentes_abertas(request):
    tarefas = Tarefa.objects.filter(
        status='ABERTA',
        prioridade='URGENTE'
    ).values()
    return JsonResponse(list(tarefas), safe=False)

# EX 5 - atrasadas
def tarefas_atrasadas(request):
    hoje = date.today()
    tarefas = Tarefa.objects.filter(
        data_entrega__lt=hoje,
        status='ABERTA'
    ).values()
    return JsonResponse(list(tarefas), safe=False)

# EX 6 - busca por palavra
def buscar_tarefas(request, palavra):
    tarefas = Tarefa.objects.filter(
        titulo__icontains=palavra
    ).values()
    return JsonResponse(list(tarefas), safe=False)
