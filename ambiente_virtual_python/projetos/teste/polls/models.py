from django.db import models

# Create your models here.

class Equipe(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    
class Integrante(models.Model):
    Equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE)
    email = models.CharField(max_length=40)
    nome_completo = models.CharField(max_length=60)

    def __str__(self):
        return self.email