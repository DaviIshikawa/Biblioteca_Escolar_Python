from django.contrib import admin
from .models import Livro


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