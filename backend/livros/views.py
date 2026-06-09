from rest_framework import viewsets
from .models import Livro
from .serializers import LivroSerializer
from django.http import JsonResponse
from django.utils import timezone
from django.db.models import F

def listar_livros(request):
    livros = Livro.objects.all().values('id', 'titulo', 'status', 'lingua', 'autor_id', autor_nome=F('autor__nome'))
    return JsonResponse(list(livros), safe=False)

def listar_livros_disponiveis(request):
    livros = Livro.objects.filter(status='DISPONIVEL').values()
    return JsonResponse(list(livros), safe=False)

def listar_livros_por_lingua(request, lingua):
    livros = Livro.objects.filter(lingua=lingua).values()
    return JsonResponse(list(livros), safe=False)

def buscar_livro_por_id(request, id):
    try:
        livro = Livro.objects.filter(id=id).values().get()
        return JsonResponse(livro)
    except Livro.DoesNotExist:
        return JsonResponse({'erro': 'Livro nao encontrado.'}, status=404)

def listar_livros_publicados_antes(request):
    hoje = timezone.now().date()
    livros = Livro.objects.filter(data_entrega__lt=hoje).values()
    return JsonResponse(list(livros), safe=False)

def buscar_livros_por_titulo(request, palavra):
    livros = Livro.objects.filter(titulo__icontains=palavra).values()
    return JsonResponse(list(livros), safe=False)

class LivroDisponivelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Livro.objects.filter(status='DISPONIVEL')
    serializer_class = LivroSerializer
