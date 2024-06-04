import os
import sys

project_root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

sys.path.append(project_root_path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
import django
django.setup()
import pandas as pd
from livros.models import Livro  

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

csv_output_path = 'exported_books.csv'  

livros = Livro.objects.all()[:200]

data = []
for livro in livros:
    data.append({
        'Title': livro.Title,
        'description': livro.description,
        'authors': livro.authors,
        'image': livro.image,
        'previewLink': livro.previewLink,
        'publisher': livro.publisher,
        'publishedDate': livro.publishedDate,
        'infoLink': livro.infoLink,
        'categories': livro.categories,
        'ratingsCount': livro.ratingsCount
    })

df = pd.DataFrame(data)

df.to_csv(csv_output_path, index=False)

print(f'Exportação para {csv_output_path} concluída com sucesso.')
