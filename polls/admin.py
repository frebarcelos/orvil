from django.contrib import admin
from .models import Livro, Resenha, Usuario, Avaliacao

admin.site.register(Livro)
admin.site.register(Resenha)
admin.site.register(Usuario)
admin.site.register(Avaliacao)

# Register your models here.
