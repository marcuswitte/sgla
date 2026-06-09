from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=255)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'autores_autor'
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
