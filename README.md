# 📚 Biblioteca Escolar - Sistema de Gerenciamento de Acervo

## Documentacao apresentativa

A documentacao completa do projeto, com resumo, objetivos, integrantes, tecnologias, funcionalidades, estrutura e conclusao, esta disponivel em [DOCUMENTACAO_APRESENTATIVA.md](DOCUMENTACAO_APRESENTATIVA.md).

## Visão Geral

**Projeto:** Biblioteca Escolar  
**Curso:** Programador Back-End Python - Desenvolvimento Web com Django  
**Escola:** Aprender Mais

Sistema web desenvolvido com **Django** para gerenciar o acervo de livros de uma escola. A aplicação oferece uma interface amigável para consultar, cadastrar, editar e excluir livros, além de integração com Django Admin para administração de dados.

---

## 📋 Requisitos Atendidos

✅ **Projeto Django funcionando**  
✅ **Banco SQLite criado automaticamente**  
✅ **Código-fonte completo**  
✅ **Interface funcionando com Bootstrap 5**  
✅ **Banco contendo 10 livros cadastrados**  
✅ **Organizado em camadas (Models, Views, Templates, URLs)**  
✅ **Django Admin para administração**  

---

## 🚀 Como Executar

### 1. Iniciar o Servidor

```bash
cd Biblioteca_Escolar_Python
python manage.py runserver
```

O servidor estará disponível em: **http://127.0.0.1:8000/**

### 2. Acessar Django Admin

- URL: http://127.0.0.1:8000/admin/
- Para criar um superusuário: `python manage.py createsuperuser`

---

## 🌐 Funcionalidades

| Página | URL | Funcionalidade |
|--------|-----|----------------|
| **Acervo** | `/` | Listagem de todos os livros |
| **Cadastrar** | `/cadastrar/` | Formulário para cadastrar novo livro |
| **Pesquisar** | `/pesquisar/` | Buscar livro por título ou autor |
| **Editar** | `/<id>/editar/` | Editar informações do livro |
| **Excluir** | `/<id>/excluir/` | Remover livro com confirmação |
| **Admin** | `/admin/` | Painel de administração |

---

## 📊 Operações CRUD

✅ **Create:** Cadastrar novo livro  
✅ **Read:** Visualizar livros  
✅ **Update:** Editar livro  
✅ **Delete:** Excluir livro com confirmação  

---

## 📁 Estrutura do Projeto

```
Biblioteca_Escolar_Python/
├── biblioteca/           # Configuração do projeto Django
├── livros/              # Aplicação principal
│   ├── models.py        # Modelo Livro
│   ├── views.py         # Views (lógica)
│   ├── urls.py          # Rotas
│   ├── admin.py         # Django Admin
│   ├── forms.py         # Formulários
│   └── templates/livros/
│       ├── base.html
│       ├── lista_livros.html
│       ├── cadastro_livro.html
│       ├── editar_livro.html
│       ├── excluir_livro.html
│       └── pesquisa.html
├── db.sqlite3           # Banco de dados
├── manage.py
└── populate_livros.py   # Script para popular dados
```

---

## 📚 Livros Cadastrados (10 no Total)

1. Dom Casmurro - Machado de Assis
2. Memórias Póstumas de Brás Cubas - Machado de Assis
3. Grande Sertão: Veredas - Guimarães Rosa
4. Gabriela, Cravo e Canela - Jorge Amado
5. Capitães da Areia - Jorge Amado
6. O Cortiço - Aluísio Azevedo
7. O Mulato - Aluísio Azevedo
8. 1984 - George Orwell
9. O Senhor dos Anéis - J.R.R. Tolkien
10. O Pequeno Príncipe - Antoine de Saint-Exupéry

---

## 🛠️ Tecnologias Utilizadas

- **Framework:** Django 6.0.6
- **Banco de Dados:** SQLite
- **Frontend:** Bootstrap 5, HTML5, CSS3
- **Linguagem:** Python 3.x
- **ORM:** Django ORM

---

## 🎨 Recursos de Interface

✅ Navbar responsiva  
✅ Cards com informações de livros  
✅ Badges de disponibilidade  
✅ Ícones Bootstrap  
✅ Busca funcional  
✅ Formulários com validação  
✅ Confirmação de exclusão  
✅ Design moderno e intuitivo  

---

## 📝 Boas Práticas Implementadas

✅ Organização em camadas (MVC)  
✅ Herança de templates  
✅ Validação de formulários  
✅ Segurança CSRF  
✅ Django Admin customizado  
✅ Interface responsiva  
✅ Código limpo e bem estruturado  

---

**Status:** ✅ Completo e Funcionando  
**Versão:** 1.0.0

