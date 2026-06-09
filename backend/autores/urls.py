from django.urls import path
from .views import (
    listar_autores,
    buscar_autor_por_id,
)

urlpatterns = [
    path('autores/', listar_autores),
    path('autores/<int:id>/', buscar_autor_por_id),
]