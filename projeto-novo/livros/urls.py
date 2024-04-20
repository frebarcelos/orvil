from django.urls import path
from livros.views import index, login,livro,buscar

urlpatterns = [
    path('',index, name='index'),
    path('login/',login, name='login'),
    path('livro/<int:livro_id>',livro, name='livro'),
    path("buscar",buscar, name='buscar')
]