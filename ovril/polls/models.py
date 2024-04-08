from django.db import models
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.

class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    senha = models.CharField(max_length=128)  # Armazena o hash da senha

    def salvar(self, *args, **kwargs):
        # Hash da senha antes de salvar no banco de dados
        if self.senha:
            self.senha = make_password(self.senha)
        super(Usuario, self).save(*args, **kwargs)

    def verificar_senha(self, senha):
        # Verifica se a senha fornecida corresponde à senha armazenada no banco de dados
        return check_password(senha, self.senha)

    def __str__(self):
        return self.nome
    
class Livro(models.Model):
    titulo = models.CharField(max_length=30)
    autor = models.CharField(max_length=50)
    genero = models.CharField(max_length=30)

    def __str__(self):
        return self.titulo

class Resenha(models.Model):
    conteudo = models.CharField(max_length=500)
    data_publicacao = models.DateField()
    usuario_id = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    licro_id = models.ForeignKey(Livro, on_delete=models.CASCADE)

class Avaliação(models.Model):
    nota = models.IntegerField()
    comentario = models.CharField(max_length=150)
    usuario_id = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    resenha_id = models.ForeignKey(Resenha, on_delete=models.CASCADE)