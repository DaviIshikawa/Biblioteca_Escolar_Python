from django.db import models


class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=150)
    editora = models.CharField(max_length=100)
    ano_publicacao = models.IntegerField()
    isbn = models.CharField(max_length=20, unique=True)
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo