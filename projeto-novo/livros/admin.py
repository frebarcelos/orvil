from django.contrib import admin

from livros.models import Livro, Resenha, Avaliacao, Usuario

class ListandoLivros(admin.ModelAdmin):
    list_display = ("id", "Title", "authors", "categories")
    list_display_links = ("id", "Title")
    search_fields = ("Title", "id", "authors", "categories")
    list_per_page = 10

class ListandoResenhas(admin.ModelAdmin):
    list_display = ("id", "titulo", "livro", "usuario", "data_publicacao", "media_avaliacoes", "num_avaliacoes_resenhas")
    list_display_links = ("id", "titulo")
    search_fields = ("titulo", "livro__Title", "usuario__nome")
    list_per_page = 10

class ListandoAvaliacoes(admin.ModelAdmin):
    list_display = ("id", "resenha", "usuario", "nota")
    list_display_links = ("id", "resenha")
    search_fields = ("resenha__titulo", "usuario__nome")
    list_per_page = 10

class ListandoUsuarios(admin.ModelAdmin):
    list_display = ("id", "nome", "email")
    list_display_links = ("id", "nome")
    search_fields = ("nome", "email")
    list_per_page = 10

admin.site.register(Livro, ListandoLivros)
admin.site.register(Resenha, ListandoResenhas)
admin.site.register(Avaliacao, ListandoAvaliacoes)
admin.site.register(Usuario, ListandoUsuarios)
