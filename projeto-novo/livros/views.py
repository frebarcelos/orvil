from django.shortcuts import render
from livros.models import Livro
from django.core.paginator import Paginator

def get_page_range(livros_pagina, num_pages_to_show=3):
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
    livros = Livro.objects.all()
    paginator = Paginator(livros, 10)
    page_number = request.GET.get('page', 1)
    livros_pagina = paginator.page(page_number)
    page_range = get_page_range(livros_pagina, num_pages_to_show=2)
    return render(request, 'livros/index.html', {"livros": livros_pagina, "page_range": page_range})

def login(request):
    return render(request, 'livros/login.html')


