from django.contrib import admin

from livros.models import Livro

class ListandoLivros(admin.ModelAdmin):
    list_display = ("id","Title","authors", "categories")
    list_display_links = ("id","Title")
    search_fields=("Title","id","authors","categories",)
    list_per_page=10

admin.site.register(Livro, ListandoLivros)
