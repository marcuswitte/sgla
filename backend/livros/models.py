from django.db import models

from autores.models import Autor

class Livro(models.Model):
	STATUS_CHOICES = [
		('DISPONIVEL', 'Disponível'),
		('EMPRESTADO', 'Emprestado'),
		('INDISPONIVEL', 'Indisponível')
	]

	LINGUA_CHOICES = [
		('PORTUGUES', 'Português'),
		('INGLES', 'Inglês'),
	]

	titulo = models.CharField(max_length=255)
	descricao = models.TextField()
	status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='DISPONIVEL')
	lingua = models.CharField(max_length=20, choices=LINGUA_CHOICES, default='PORTUGUES')
	data_criacao = models.DateTimeField(auto_now_add=True)
	data_entrega = models.DateField()
	autor = models.ForeignKey(Autor, blank=True, null=True, on_delete=models.SET_NULL, related_name='livros')

	def __str__(self):
		return self.titulo

	class Meta:
		db_table = 'livros_livro'
		verbose_name = 'Livro'
		verbose_name_plural = 'Livros'