from django.urls import path
from .views import (
    listar_livros,
    listar_livros_disponiveis,
    listar_livros_por_lingua,
    buscar_livro_por_id,
    listar_livros_publicados_antes,
    buscar_livros_por_titulo,
)

urlpatterns = [
    path('livros/', listar_livros),
    path('livros/disponiveis/', listar_livros_disponiveis),
    path('livros/lingua/<str:lingua>/', listar_livros_por_lingua),
    path('livros/anteriores/', listar_livros_publicados_antes),
    path('livros/busca/<str:palavra>/', buscar_livros_por_titulo),
    path('livros/<int:id>/', buscar_livro_por_id),
]