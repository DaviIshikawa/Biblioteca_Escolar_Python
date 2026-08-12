import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "biblioteca.settings")
django.setup()

from livros.models import Livro

# Livros clássicos da literatura brasileira e mundial
livros_data = [
    {
        "titulo": "Memórias Póstumas de Brás Cubas",
        "autor": "Machado de Assis",
        "editora": "Editora 34",
        "ano_publicacao": 1899,
        "isbn": "978-8534900005",
        "disponivel": True,
    },
    {
        "titulo": "Grande Sertão: Veredas",
        "autor": "Guimarães Rosa",
        "editora": "Instituto Moreira Salles",
        "ano_publicacao": 1956,
        "isbn": "978-8588197305",
        "disponivel": True,
    },
    {
        "titulo": "Gabriela, Cravo e Canela",
        "autor": "Jorge Amado",
        "editora": "Companhia das Letras",
        "ano_publicacao": 1958,
        "isbn": "978-8535929607",
        "disponivel": False,
    },
    {
        "titulo": "Capitães da Areia",
        "autor": "Jorge Amado",
        "editora": "Companhia das Letras",
        "ano_publicacao": 1937,
        "isbn": "978-8535925524",
        "disponivel": True,
    },
    {
        "titulo": "O Cortiço",
        "autor": "Aluísio Azevedo",
        "editora": "Editora Globo",
        "ano_publicacao": 1890,
        "isbn": "978-8525053378",
        "disponivel": True,
    },
    {
        "titulo": "O Mulato",
        "autor": "Aluísio Azevedo",
        "editora": "Editora L&PM",
        "ano_publicacao": 1881,
        "isbn": "978-8525416549",
        "disponivel": False,
    },
    {
        "titulo": "1984",
        "autor": "George Orwell",
        "editora": "Editora Rocco",
        "ano_publicacao": 1949,
        "isbn": "978-8532530786",
        "disponivel": True,
    },
    {
        "titulo": "O Senhor dos Anéis",
        "autor": "J.R.R. Tolkien",
        "editora": "Editora Aleph",
        "ano_publicacao": 1954,
        "isbn": "978-8584840008",
        "disponivel": True,
    },
    {
        "titulo": "O Pequeno Príncipe",
        "autor": "Antoine de Saint-Exupéry",
        "editora": "Editora Intrínseca",
        "ano_publicacao": 1943,
        "isbn": "978-8525403037",
        "disponivel": True,
    },
]

# Inserir livros que não existem
livros_criados = 0
for livro_data in livros_data:
    if not Livro.objects.filter(isbn=livro_data["isbn"]).exists():
        Livro.objects.create(**livro_data)
        livros_criados += 1
        print(f"✓ Livro criado: {livro_data['titulo']}")
    else:
        print(f"→ Livro já existe: {livro_data['titulo']}")

print(f"\n📚 Total de livros criados: {livros_criados}")
print(f"📊 Total de livros no banco: {Livro.objects.count()}")
