from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from .models import Livro, Usuario
from .forms import LivroForm, UsuarioForm


def lista_livros(request):
    livros = Livro.objects.all()

    return render(
        request,
        'livros/lista_livros.html',
        {'livros': livros}
    )


def cadastrar_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('lista_livros')

    else:
        form = LivroForm()

    return render(
        request,
        'livros/cadastro_livro.html',
        {'form': form}
    )


def editar_livro(request, id):
    livro = get_object_or_404(Livro, id=id)

    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)

        if form.is_valid():
            form.save()
            return redirect('lista_livros')

    else:
        form = LivroForm(instance=livro)

    return render(
        request,
        'livros/editar_livro.html',
        {'form': form, 'livro': livro}
    )


def excluir_livro(request, id):
    livro = get_object_or_404(Livro, id=id)

    if request.method == 'POST':
        livro.delete()
        return redirect('lista_livros')

    return render(
        request,
        'livros/excluir_livro.html',
        {'livro': livro}
    )


def pesquisar_livros(request):
    termo = request.GET.get('q', '').strip()
    disponibilidade = request.GET.get('disponivel', '')

    livros = Livro.objects.all()

    if termo:
        livros = livros.filter(
            Q(titulo__icontains=termo) |
            Q(autor__icontains=termo) |
            Q(isbn__icontains=termo)
        )

    if disponibilidade == 'sim':
        livros = livros.filter(disponivel=True)

    elif disponibilidade == 'nao':
        livros = livros.filter(disponivel=False)

    return render(
        request,
        'livros/pesquisa.html',
        {
            'livros': livros,
            'termo': termo,
            'disponibilidade': disponibilidade,
        }
    )


def lista_usuarios(request):
    termo = request.GET.get('q', '').strip()

    usuarios = Usuario.objects.all()

    if termo:
        usuarios = usuarios.filter(
            Q(nome__icontains=termo) |
            Q(email__icontains=termo) |
            Q(cpf__icontains=termo) |
            Q(matricula__icontains=termo)
        )

    return render(
        request,
        'livros/lista_usuarios.html',
        {'usuarios': usuarios, 'termo': termo}
    )


def cadastrar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')

    else:
        form = UsuarioForm()

    return render(
        request,
        'livros/cadastro_usuario.html',
        {'form': form}
    )


def editar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)

    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)

        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')

    else:
        form = UsuarioForm(instance=usuario)

    return render(
        request,
        'livros/editar_usuario.html',
        {'form': form, 'usuario': usuario}
    )


def excluir_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)

    if request.method == 'POST':
        usuario.delete()
        return redirect('lista_usuarios')

    return render(
        request,
        'livros/excluir_usuario.html',
        {'usuario': usuario}
    )