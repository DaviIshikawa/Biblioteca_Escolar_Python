from django.contrib import admin
from .models import Livro, Usuario


@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = (
        'titulo',
        'autor',
        'editora',
        'ano_publicacao',
        'disponivel'
    )

    list_filter = (
        'disponivel',
        'editora',
    )

    search_fields = (
        'titulo',
        'autor',
        'isbn',
    )

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'matricula', 'email', 'turma', 'ativo', 'data_cadastro')
    list_filter = ('ativo', 'turma')
    search_fields = ('nome', 'cpf', 'matricula', 'email')
    list_editable = ('ativo',)