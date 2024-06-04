import os

# Obtém o diretório atual do script
script_directory = os.path.dirname(os.path.abspath(__file__))

# Constrói o caminho absoluto para o arquivo CSV
csv_file_path = os.path.join(script_directory, 'exported_books.csv')

print("Caminho absoluto para o arquivo CSV:", csv_file_path)
