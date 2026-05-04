from django.http import JsonResponse
from .models import Usuario

def listar_usuarios(request):
    usuarios = Usuario.objects.all().values()
    return JsonResponse(list(usuarios), safe=False)

def buscar_usuario_por_id(request, id):
    try:
        usuario = Usuario.objects.get(id=id)
        return JsonResponse({
            "id": usuario.id,
            "nome": usuario.nome,
            "email": usuario.email,
            "ativo": usuario.ativo
        })
    except Usuario.DoesNotExist:
        return JsonResponse({"erro": "Usuário não encontrado"}, status=404)
