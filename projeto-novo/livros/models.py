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