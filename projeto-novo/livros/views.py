from django.shortcuts import render
from livros.models import Livro


def index(request):
    livros = Livro.objects.all()
    return render(request, 'livros/index.html', {"livros": livros})

def login(request):
    return render(request, 'livros/login.html')


