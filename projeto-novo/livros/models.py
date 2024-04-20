from django.db import models
from django.db.models import Avg 
from django.contrib.auth.models import User

class Livro(models.Model):
    Title = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=300, null=False, blank=False)
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
    

class Resenha(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(to=User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255, null=False, blank=False)
    texto = models.TextField(null=False, blank=False)
    data_publicacao = models.DateTimeField(auto_now_add=True)
    media_avaliacoes = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    num_avaliacoes_resenhas = models.IntegerField(default=0)

    def calcular_media_avaliacoes(self):
        media = Avaliacao.objects.filter(resenha=self).aggregate(media=Avg('nota'))['media']
        self.media_avaliacoes = media or 0  
        self.save()

    def calcular_num_avaliacoes_resenhas(self):
        num_avaliacoes_resenhas = Avaliacao.objects.filter(resenha=self).count()
        self.num_avaliacoes_resenhas = num_avaliacoes_resenhas
        self.save()

    def __str__(self):
        return f"Resenha de '{self.livro.Title}' por {self.usuario.username}"

class Avaliacao(models.Model):
    resenha = models.ForeignKey(Resenha, on_delete=models.CASCADE)
    usuario = models.ForeignKey(to=User, on_delete=models.CASCADE)
    nota = models.CharField(max_length=9, null=False, blank=False, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.resenha.calcular_media_avaliacoes()
        self.resenha.calcular_num_avaliacoes_resenhas()

    def __str__(self):
        return f"Avaliação de '{self.resenha.titulo}' por {self.usuario.username}"
