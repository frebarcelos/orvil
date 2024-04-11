from django.db import models

class User(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    senha = models.CharField(max_length=128)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'polls_users'