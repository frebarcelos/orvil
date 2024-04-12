from django.urls import path
from ..view.BookView import createBook, getBook, deleteBook, editBook, listBooks,listGenderBooks,listAutorBooks

urlpatterns = [
    path('cadastrar/', createBook, name='createUser'),
    path('informacoes/', getBook, name='informacoesLivro'),
    path('remover/', deleteBook, name='remover'),
    path('editar/', editBook, name = 'editar'),
    path('list/', listBooks, name = 'listar'),
    path('autor/', listAutorBooks, name = 'listar'),
    path('genero/', listGenderBooks, name = 'listar')
]