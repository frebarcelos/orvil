from django.urls import path
from livros.views import index, login,livro,buscar,cadastro,logout

urlpatterns = [
    path('',index, name='index'),
    path('login/',login, name='login'),
    path('cadastro/',cadastro, name='cadastro'),
    path('livro/<int:livro_id>',livro, name='livro'),
    path("buscar",buscar, name='buscar'),
    path('login', login, name='login'),
    path('cadastro', cadastro, name='cadastro'),
    path('logout', logout, name='logout'),
]