import os
import sys

project_root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

sys.path.append(project_root_path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
import django
django.setup()
import pandas as pd
from livros.models import Livro

csv_file_path = 'exported_books.csv'  
df = pd.read_csv(csv_file_path)

imported_count = 0

index = 0
while imported_count < 200 and index < len(df):
    row = df.iloc[index]

    if row.notnull().all():
        
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
        
        imported_count += 1

    
    index += 1

print(f"{imported_count} registros completos foram importados com sucesso.")
