from django.db import models

class Livro(models.Model):
    Title = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=100, null=False, blank=False)
    authors = models.CharField(max_length=100, null=False, blank=False)
    image = models.CharField(max_length=100, null=False, blank=False)
    previewLink = models.CharField(max_length=100, null=False, blank=False)
    publisher = models.CharField(max_length=100, null=False, blank=False)
    publishedDate = models.CharField(max_length=100, null=False, blank=False)
    infoLink = models.CharField(max_length=100, null=False, blank=False)
    categories = models.CharField(max_length=100, null=False, blank=False)
    ratingsCount = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self) -> str:
        return f"Livro [titulo={self.Title}]"
    
class Usuario(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=255, null=False, blank=False)
    senha = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.nome


class Resenha(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255, null=False, blank=False)
    texto = models.TextField(null=False, blank=False)
    data_publicacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Resenha de '{self.livro.Title}' por {self.usuario.nome}"


class Avaliacao(models.Model):
    resenha = models.ForeignKey(Resenha, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nota = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False)

    def __str__(self):
        return f"Avaliação de '{self.resenha.titulo}' por {self.usuario.nome}"