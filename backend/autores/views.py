from .models import Autor
from django.http import JsonResponse

def listar_autores(request):
    autores = Autor.objects.all().values()
    return JsonResponse(list(autores), safe=False)

def buscar_autor_por_id(request, id):
    try:
        autor = Autor.objects.filter(id=id).values().get()
        return JsonResponse(autor)
    except Autor.DoesNotExist:
        return JsonResponse({'erro': 'Autor nao encontrado.'}, status=404)