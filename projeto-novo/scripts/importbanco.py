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
from livros.models import Livro

# Caminho para o arquivo CSV
csv_file_path = 'exported_books.csv'  # Substitua pelo caminho do seu arquivo CSV

# Leia o arquivo CSV
df = pd.read_csv(csv_file_path)

# Inicialize um contador de registros completos importados
imported_count = 0

# Itere sobre as linhas do DataFrame para encontrar 200 registros completos
index = 0
while imported_count < 200 and index < len(df):
    row = df.iloc[index]

    # Verifique se a linha não contém valores nulos
    if row.notnull().all():
        # Crie ou atualize um registro no banco de dados
        Livro.objects.update_or_create(
            Title=row['Title'],
            defaults={
                'description': row['description'],
                'authors': row['authors'],
                'image': row['image'],
                'previewLink': row['previewLink'],
                'publisher': row['publisher'],
                'publishedDate': row['publishedDate'],
                'infoLink': row['infoLink'],
                'categories': row['categories'],
                'ratingsCount': row['ratingsCount']
            }
        )
        # Aumente o contador de registros completos importados
        imported_count += 1

    # Avance para a próxima linha
    index += 1

print(f"{imported_count} registros completos foram importados com sucesso.")
