from django.urls import path
from . import views


urlpatterns = [
    path(
        '',
        views.lista_livros,
        name='lista_livros'
    ),

    path(
        'cadastrar/',
        views.cadastrar_livro,
        name='cadastrar_livro'
    ),

    path(
        'pesquisar/',
        views.pesquisar_livros,
        name='pesquisar_livros'
    ),

    path(
        'editar/<int:id>/',
        views.editar_livro,
        name='editar_livro'
    ),

    path(
        'excluir/<int:id>/',
        views.excluir_livro,
        name='excluir_livro'
    ),

        path(
        'usuarios/',
        views.lista_usuarios,
        name='lista_usuarios'
    ),

    path(
        'usuarios/cadastrar/',
        views.cadastrar_usuario,
        name='cadastrar_usuario'
    ),

    path(
        'usuarios/editar/<int:id>/',
        views.editar_usuario,
        name='editar_usuario'
    ),

    path(
        'usuarios/excluir/<int:id>/',
        views.excluir_usuario,
        name='excluir_usuario'
    ),
]