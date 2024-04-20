from livros.models import Livro

class CategoriasMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        categorias_disponiveis = Livro.objects.values_list('categories', flat=True).distinct().order_by('categories')
        request.categorias_disponiveis = categorias_disponiveis
        response = self.get_response(request)
        return response