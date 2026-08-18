from django import forms
from .models import Livro, Usuario


class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = [
            'titulo',
            'autor',
            'editora',
            'ano_publicacao',
            'isbn',
            'disponivel',
        ]
class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'nome',
            'email',
            'cpf',
            'matricula',
            'turma',
            'telefone',
            'ativo',
        ]