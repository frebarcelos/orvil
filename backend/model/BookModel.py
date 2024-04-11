from django.db import models

class Book(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=50, unique=True)
    genero = models.CharField(max_length=50)

    def __str__(self):
        return self.titulo

    class Meta:
        db_table = 'polls_books'