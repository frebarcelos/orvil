import os
import sys

project_root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

sys.path.append(project_root_path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
import django
django.setup()

import re

from livros.models import Livro

livros = Livro.objects.all()

regex = re.compile(r'\r')

count_alteracoes = 0

for livro in livros:
    if '[' in livro.authors or ']' in livro.authors:
        livro.authors = re.sub(r'\[\'|\']', '', livro.authors)
        count_alteracoes += 1

    if '[' in livro.categories or ']' in livro.categories:
        livro.categories = re.sub(r'\[\'|\']', '', livro.categories)
        count_alteracoes += 1

    livro.save()

print(f"Número total de alterações feitas: {count_alteracoes}")
