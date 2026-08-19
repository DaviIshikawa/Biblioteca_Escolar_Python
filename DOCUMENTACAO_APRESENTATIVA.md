# BIBLIOTECA ESCOLAR
## Sistema de Gerenciamento de Acervo

**Documentacao apresentativa do projeto**

**Integrantes:**

- Davi Ishikawa
- Bernardo Gabriel
- Rodrigo Nascimento

**GitHub:** https://github.com/DaviIshikawa

**Curso:** Programador Back-End Python - Desenvolvimento Web com Django

**Instituicao:** Escola Aprender Mais

---

# 1. Resumo

O projeto Biblioteca Escolar consiste em um sistema web desenvolvido para auxiliar no gerenciamento de uma biblioteca escolar. A aplicacao permite cadastrar, consultar, editar e excluir livros, alem de manter o cadastro de usuarios, como alunos e leitores.

O sistema foi desenvolvido utilizando o framework Django, da linguagem Python, e possui uma interface web responsiva criada com HTML, CSS e Bootstrap. O banco de dados utilizado e o SQLite, uma opcao simples e adequada para o desenvolvimento e para a apresentacao academica do projeto.

A proposta principal e organizar as informacoes da biblioteca em um unico sistema, facilitando a consulta do acervo e o controle da disponibilidade dos livros.

# 2. Introducao

Bibliotecas escolares precisam manter organizadas as informacoes sobre seus livros e usuarios. Quando esses dados sao controlados manualmente, podem ocorrer dificuldades para localizar um livro, verificar sua disponibilidade ou atualizar o cadastro de um aluno.

Pensando nesse problema, foi desenvolvido o sistema Biblioteca Escolar. A aplicacao oferece uma estrutura digital para o controle do acervo e dos usuarios, tornando as tarefas de cadastro e consulta mais rapidas e organizadas.

O projeto tambem demonstra, na pratica, a utilizacao de conceitos importantes do desenvolvimento web com Django, como modelos, formularios, views, rotas, templates, banco de dados e painel administrativo.

# 3. Problema identificado

O controle manual de uma biblioteca pode causar alguns problemas, tais como:

- Dificuldade para localizar livros no acervo.
- Falta de informacao sobre a disponibilidade de cada livro.
- Registros de usuarios desorganizados.
- Maior possibilidade de erros durante a atualizacao dos dados.
- Demora para cadastrar, editar ou excluir informacoes.
- Falta de um painel centralizado para administrar os registros.

# 4. Justificativa

A criacao de um sistema web para a biblioteca contribui para a organizacao das informacoes e para a melhoria do acesso aos dados. Com a aplicacao, o responsavel pela biblioteca consegue visualizar os livros cadastrados, realizar pesquisas e administrar os registros de usuarios em uma unica interface.

A escolha do Django ocorreu porque o framework oferece recursos importantes para o desenvolvimento de aplicacoes web, como sistema de rotas, ORM, formularios, autenticacao administrativa, protecao CSRF e estrutura organizada em aplicacoes.

# 5. Objetivos

## 5.1 Objetivo geral

Desenvolver um sistema web para gerenciar o acervo de livros e o cadastro de usuarios de uma biblioteca escolar.

## 5.2 Objetivos especificos

- Cadastrar livros com informacoes completas.
- Consultar os livros existentes no acervo.
- Pesquisar livros por titulo, autor ou ISBN.
- Filtrar livros de acordo com a disponibilidade.
- Editar informacoes dos livros cadastrados.
- Excluir livros mediante confirmacao.
- Cadastrar alunos e demais usuarios da biblioteca.
- Pesquisar usuarios por nome, email, CPF ou matricula.
- Controlar a situacao dos usuarios como ativos ou inativos.
- Disponibilizar um painel administrativo por meio do Django Admin.
- Aplicar uma estrutura organizada de desenvolvimento web.

# 6. Tecnologias utilizadas

- **Linguagem:** Python 3.x
- **Framework:** Django 6.1
- **Banco de dados:** SQLite
- **ORM:** Django ORM
- **Frontend:** HTML5 e CSS3
- **Estilizacao:** Bootstrap 5.3.3
- **Icones:** Bootstrap Icons 1.11.0
- **Controle de arquivos:** Git e GitHub

As dependencias principais do projeto estao registradas no arquivo `requirements.txt`.

# 7. Funcionamento do sistema

O funcionamento da aplicacao segue o fluxo abaixo:

1. O usuario acessa uma pagina por meio de uma URL.
2. O Django identifica a rota correspondente em `livros/urls.py`.
3. A requisicao e encaminhada para uma view em `livros/views.py`.
4. A view consulta ou altera os dados utilizando os modelos do Django.
5. Os formularios validam as informacoes antes do armazenamento.
6. O template HTML apresenta o resultado ao usuario.
7. Depois de uma operacao concluida, o sistema redireciona para a pagina adequada.

Esse fluxo separa as responsabilidades do sistema e facilita a manutencao do codigo.

# 8. Principais funcionalidades

## 8.1 Gerenciamento de livros

O sistema permite:

- Visualizar o acervo completo.
- Cadastrar um novo livro.
- Editar os dados de um livro.
- Excluir um livro com pagina de confirmacao.
- Informar se o livro esta disponivel ou indisponivel.
- Exibir titulo, autor, editora, ano de publicacao e ISBN.

## 8.2 Pesquisa de livros

A pesquisa de livros aceita um termo e verifica os campos de titulo, autor e ISBN. A busca nao diferencia letras maiusculas de minusculas.

Tambem e possivel filtrar os resultados por disponibilidade, utilizando as opcoes de livros disponiveis ou indisponiveis.

## 8.3 Gerenciamento de usuarios

O cadastro de usuarios possui os seguintes dados:

- Nome.
- Email.
- CPF.
- Matricula.
- Turma.
- Telefone.
- Situacao ativa ou inativa.
- Data de cadastro preenchida automaticamente.

A listagem permite pesquisar por nome, email, CPF ou matricula e possui opcoes para editar e excluir registros.

## 8.4 Painel administrativo

O Django Admin esta configurado para os modelos `Livro` e `Usuario`. No painel, e possivel consultar os registros, realizar pesquisas, utilizar filtros e administrar os dados diretamente.

# 9. Modelos do banco de dados

## 9.1 Modelo Livro

O modelo `Livro` representa cada item cadastrado no acervo. Ele possui os seguintes campos:

- `titulo`: nome do livro.
- `autor`: nome do autor.
- `editora`: editora responsavel pela publicacao.
- `ano_publicacao`: ano em que o livro foi publicado.
- `isbn`: identificador unico do livro.
- `disponivel`: informa se o livro esta disponivel.

O ISBN e unico, evitando o cadastro duplicado do mesmo identificador.

## 9.2 Modelo Usuario

O modelo `Usuario` representa os leitores cadastrados na biblioteca. Ele possui os seguintes campos:

- `nome`: nome completo do usuario.
- `email`: endereco de email, com valor unico.
- `cpf`: documento de identificacao, com valor unico.
- `matricula`: matricula escolar, com valor unico.
- `turma`: turma do usuario, quando informada.
- `telefone`: telefone para contato, quando informado.
- `data_cadastro`: preenchida automaticamente na criacao.
- `ativo`: indica se o cadastro esta ativo.

# 10. Operacoes CRUD

O projeto implementa as quatro operacoes fundamentais de persistencia de dados:

- **Create:** cadastro de livros e usuarios.
- **Read:** visualizacao das listas e pesquisas.
- **Update:** edicao de livros e usuarios.
- **Delete:** exclusao de registros com confirmacao.

# 11. Rotas principais

| Metodo | Rota | Funcao |
|---|---|---|
| GET | `/` | Lista o acervo de livros |
| GET/POST | `/cadastrar/` | Cadastra um livro |
| GET | `/pesquisar/` | Pesquisa livros e disponibilidade |
| GET/POST | `/editar/<id>/` | Edita um livro |
| GET/POST | `/excluir/<id>/` | Exclui um livro |
| GET | `/usuarios/` | Lista e pesquisa usuarios |
| GET/POST | `/usuarios/cadastrar/` | Cadastra um usuario |
| GET/POST | `/usuarios/editar/<id>/` | Edita um usuario |
| GET/POST | `/usuarios/excluir/<id>/` | Exclui um usuario |
| GET | `/admin/` | Acessa o painel administrativo |

# 12. Estrutura do projeto

```text
Biblioteca_Escolar_Python/
|-- biblioteca/
|   |-- settings.py       Configuracoes do projeto
|   |-- urls.py            Rotas principais
|   |-- asgi.py            Entrada para servidores ASGI
|   |-- wsgi.py            Entrada para servidores WSGI
|-- livros/
|   |-- models.py          Modelos Livro e Usuario
|   |-- forms.py            Formularios da aplicacao
|   |-- views.py            Logica das paginas
|   |-- urls.py             Rotas de livros e usuarios
|   |-- admin.py            Configuracao do Django Admin
|   |-- migrations/         Historico das alteracoes do banco
|   |-- templates/livros/   Paginas HTML do sistema
|-- static/                 Arquivos estaticos
|-- db.sqlite3              Banco de dados local
|-- manage.py               Utilitario de comandos Django
|-- populate_livros.py      Script com livros de exemplo
|-- requirements.txt        Dependencias do projeto
|-- README.md               Resumo do projeto
|-- DOCUMENTACAO_APRESENTATIVA.md  Este documento
```

# 13. Interface do sistema

A interface foi desenvolvida para ser simples e responsiva. Entre os recursos visuais, estao:

- Barra de navegacao com acesso ao acervo, cadastro, pesquisa, usuarios e administracao.
- Cards para apresentar livros e usuarios.
- Indicadores de disponibilidade dos livros.
- Indicadores de usuarios ativos e inativos.
- Formularios com validacao.
- Botoes para editar e excluir registros.
- Paginas de confirmacao antes da exclusao.
- Layout adaptavel para diferentes tamanhos de tela.

# 14. Como executar o projeto

## 14.1 Criacao do ambiente virtual

No PowerShell do Windows:

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

No Git Bash:

```bash
python -m venv venv
source venv/Scripts/activate
```

## 14.2 Instalacao das dependencias

Na pasta raiz do projeto, execute:

```bash
python -m pip install -r requirements.txt
```

## 14.3 Atualizacao do banco

```bash
python manage.py migrate
```

## 14.4 Insercao de livros de exemplo

```bash
python populate_livros.py
```

O script verifica o ISBN de cada livro antes de realizar a insercao, evitando duplicidades.

## 14.5 Inicializacao do servidor

```bash
python manage.py runserver
```

Depois, acesse o endereco:

```text
http://127.0.0.1:8000/
```

# 15. Acesso ao Django Admin

Para criar um usuario administrador, execute:

```bash
python manage.py createsuperuser
```

Depois de preencher os dados solicitados, acesse:

```text
http://127.0.0.1:8000/admin/
```

O painel permite administrar livros e usuarios com filtros e campos de pesquisa.

# 16. Verificacao e testes

Para verificar se a configuracao do Django esta correta:

```bash
python manage.py check
```

Para executar os testes automatizados:

```bash
python manage.py test
```

O arquivo `livros/tests.py` esta preparado para receber novos testes. A ampliacao dos testes pode validar o cadastro, a pesquisa, a edicao, a exclusao e as regras de unicidade dos campos.

# 17. Resultados esperados

Com o sistema em funcionamento, espera-se que a biblioteca consiga:

- Localizar livros de maneira mais rapida.
- Identificar quais livros estao disponiveis.
- Manter os cadastros atualizados.
- Reduzir erros de preenchimento por meio da validacao dos formularios.
- Organizar os dados em um banco de dados estruturado.
- Administrar livros e usuarios por uma interface web.

# 18. Possibilidades de melhoria

Como evolucoes futuras, o projeto pode receber:

- Cadastro de emprestimos e devolucoes.
- Relacionamento entre usuarios e livros emprestados.
- Controle de prazos e atrasos.
- Historico de movimentacoes.
- Sistema de autenticacao para diferentes tipos de usuario.
- Relatorios do acervo e dos emprestimos.
- Paginacao para listas extensas.
- Testes automatizados mais completos.
- Publicacao em um ambiente de producao.

# 19. Conclusao

O projeto Biblioteca Escolar apresenta uma solucao funcional para o gerenciamento basico de uma biblioteca escolar. A aplicacao reune cadastro de livros, pesquisa, controle de disponibilidade, cadastro de usuarios e painel administrativo em um unico sistema.

Durante o desenvolvimento, foram aplicados conceitos de Python, Django, banco de dados, desenvolvimento web, organizacao de codigo e operacoes CRUD. O resultado e uma base que atende ao objetivo academico do projeto e que pode ser ampliada com recursos de emprestimos, devolucoes e relatorios.

A participacao de Davi Ishikawa, Bernardo Gabriel e Rodrigo Nascimento contribuiu para a construcao da proposta, e o projeto pode ser acompanhado pelo GitHub em:

**https://github.com/DaviIshikawa**

---

**Projeto:** Biblioteca Escolar

**Equipe:** Davi Ishikawa, Bernardo Gabriel e Rodrigo Nascimento

**Versao:** 1.0.0
