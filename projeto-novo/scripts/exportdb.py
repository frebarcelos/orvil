import os
import sys

# Caminho para o diretório raiz do projeto
project_root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Adicione o diretório raiz ao sys.path
sys.path.append(project_root_path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
import django
django.setup()
import pandas as pd
from livros.models import Livro  # Importe o modelo apropriado

# Defina o módulo de configurações do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

# Defina o caminho para o arquivo CSV de saída
csv_output_path = 'exported_books.csv'  # Substitua pelo caminho desejado para o arquivo CSV

# Obtenha os primeiros 200 registros do banco de dados
livros = Livro.objects.all()[:200]

# Crie uma lista de dicionários para armazenar os dados
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

# Converta os dados para um DataFrame do pandas
df = pd.DataFrame(data)

# Exporte o DataFrame para um arquivo CSV
df.to_csv(csv_output_path, index=False)

print(f'Exportação para {csv_output_path} concluída com sucesso.')
