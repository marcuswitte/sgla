from rest_framework import serializers
from .models import Livro

class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = ['id', 'titulo', 'descricao', 'status', 'lingua', 'data_criacao', 'data_entrega', 'autor']
