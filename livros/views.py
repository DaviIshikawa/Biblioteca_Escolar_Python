from django.shortcuts import render, redirect, get_object_or_404
from .models import Livro
from .forms import LivroForm


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
    termo = request.GET.get('q', '')
    disponibilidade = request.GET.get('disponivel', '')

    livros = Livro.objects.filter(
        titulo__icontains=termo
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