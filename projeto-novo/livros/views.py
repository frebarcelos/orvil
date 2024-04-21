from django.shortcuts import render, get_object_or_404, redirect
from livros.models import Livro, Resenha
from django.core.paginator import Paginator
from urllib.parse import urlencode
from livros.forms import LoginForms, CadastroForms,ResenhaForms
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

def get_page_range(livros_pagina, num_pages_to_show=1):
    total_pages = livros_pagina.paginator.num_pages
    current_page = livros_pagina.number    

    start_page = max(current_page - num_pages_to_show, 1)
    end_page = min(current_page + num_pages_to_show, total_pages)    

    page_range = list(range(start_page, end_page + 1))
    
    if 1 not in page_range:
        page_range.insert(0, 1)
        if 2 not in page_range:
            page_range.insert(1, '...')    

    if total_pages not in page_range:
        if total_pages - 1 not in page_range:
            page_range.append('...')
        page_range.append(total_pages)
    
    return page_range


def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')
    livros = Livro.objects.all()
    paginator = Paginator(livros, 10)
    page_number = request.GET.get('page', 1)
    livros_pagina = paginator.page(page_number)
    page_range = get_page_range(livros_pagina, num_pages_to_show=2)
    return render(request, 'livros/index.html', {"livros": livros_pagina, "page_range": page_range})

def livro(request, livro_id):
    form = ResenhaForms()
    livro = get_object_or_404(Livro, pk=livro_id)
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')
    if request.method == 'POST':
        form = ResenhaForms(request.POST)
        if form.is_valid():
            titulo = form['titulo_resenha'].value()
            texto = form['texto_resenha'].value()
            usuario = request.user

            resenha = Resenha.objects.create(livro=livro, usuario=usuario, titulo=titulo, texto=texto)
            resenha.calcular_media_avaliacoes()
            resenha.calcular_num_avaliacoes_resenhas()
   
    resenhas = Resenha.objects.filter(livro=livro)
    return render(request, 'livros/livro.html', {"livro": livro, "resenhas": resenhas, "form": form})

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')
    livros = Livro.objects.all()
    categoria_selecionada = request.GET.get('categoria')
    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:           
            livros = livros.filter(Title__icontains=nome_a_buscar) | \
                     livros.filter(authors__icontains=nome_a_buscar) | \
                     livros.filter(publisher__icontains=nome_a_buscar)                      
    if "categoria" in request.GET:
        categoria = request.GET['categoria']
        if categoria:
            livros = livros.filter(categories__icontains=categoria)
    if "ordem" in request.GET:
        ordem = request.GET['ordem']
        if ordem:
            livros = livros.order_by(ordem)
    paginator = Paginator(livros, 10)
    page_number = request.GET.get('page', 1)
    livros_pagina = paginator.page(page_number)
    page_range = paginator.page_range
    return render(request, 'livros/buscar.html', {"livros": livros_pagina, "page_range": page_range, 'parametros_da_busca': urlencode(request.GET)})

#sistema de login :

def login(request):
        form = LoginForms()

        if request.method == 'POST':
            form = LoginForms(request.POST)

            if form.is_valid():
                nome = form['nome_login'].value()
                senha = form['senha'].value()

            usuario = auth.authenticate(
                request,
                username=nome,
                password=senha
            )
            if usuario is not None:
                auth.login(request, usuario)
                messages.success(request, f'{nome} logado com sucesso!')
                return redirect('index')
            else:
                messages.error(request, 'Usuário ou senha incorretos')
                return redirect('login')
        
        return render(request, "livros/login.html", {"form": form})

def cadastro(request):
    form = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)

        if form.is_valid():
            if form["senha_1"].value() != form["senha_2"].value():
                messages.error(request, 'Senhas não são iguais')
                return redirect('cadastro')

            nome=form['nome_cadastro'].value()
            email=form['email'].value()
            senha=form['senha_1'].value()

            if User.objects.filter(username=nome).exists():
                messages.error(request, 'Usuário já existente')
                return redirect('cadastro')

            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            usuario.save()
            messages.success(request, 'Cadastro efetuado com sucesso!')
            return redirect('login')

    return render(request, 'livros/cadastro.html', {'form': form})

def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout efetuado com sucesso!')
    return redirect('login')

