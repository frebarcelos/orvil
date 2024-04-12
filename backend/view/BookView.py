from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from ..dao.BookDAO import BookDAO

@csrf_exempt
def createBook(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        if data:
            titulo = data['titulo']
            autor = data['autor']
            genero = data['genero']
            if BookDAO.getBookByTitle(titulo):
                return JsonResponse({'Error': 'This book is already registered'}, safe=False, status=400)
            BookDAO.createBook(titulo, autor, genero)
            returnedData = {'Titulo' : titulo, 'Autor' : autor, 'Genero' : genero, 'Mensagem': 'Livro registrado com sucesso'}
            return JsonResponse(returnedData, safe=False, status=201)
    else:
        return HttpResponse(status=405)

@csrf_exempt
def getBook(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        if data:
            id = data['id']
            book = BookDAO.getBookById(id)
            if book:
                return JsonResponse({'Titulo' : book.titulo, 'Autor' : book.autor, 'Genero' : book.genero}, safe=False,status=200)
            return JsonResponse({'Error' : 'Book not found'}, safe=False, status=404)
        return HttpResponse(status=400)
    else:
        return HttpResponse(status=405)

@csrf_exempt
def editBook(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        if data:
            id = data['id']
            titulo = data['titulo']
            autor = data['autor']
            genero = data['genero']
            book = BookDAO.getBookById(id)
            if book:
                editedBook = BookDAO.updateBook(id,titulo, autor,genero)
                if editedBook:
                    print(editedBook)
                    return JsonResponse({'Message' : 'Book edited successfully'}, safe=False,status=200)
            return JsonResponse({'Error' : 'Book not found'}, safe=False, status=404)
        return HttpResponse(status=400)
    else:
        return HttpResponse(status=405)

@csrf_exempt
def deleteBook(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        if data:
            id = data['id']
            book = BookDAO.getBookById(id)
            if book:
                deletedBook = BookDAO.deleteBook(id)
                if deletedBook:
                    return JsonResponse({'Message' : 'Book deleted successfully'}, safe=False,status=200)
            return JsonResponse({'Error' : 'Book not found'}, safe=False, status=404)
        return HttpResponse(status=400)
    else:
        return HttpResponse(status=405)

@csrf_exempt
def listBooks(request):
    if request.method == 'GET':
        books = BookDAO.getAllBooks()
        allBooks =[]
        for book in books:
            allBooks.append({'Id': book.id, 'Titulo' : book.titulo, 'Autor' : book.autor, 'Genero' : book.genero})
        return JsonResponse(allBooks, safe=False, status=200)
    else:
        return HttpResponse(status=405)

@csrf_exempt
def listAutorBooks(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        if data:
            author = data['autor']
            books = BookDAO.getBooksByAuthor(author)
            if books:
                allBooks = []
                for book in books:
                    allBooks.append({'Id': book.id, 'Titulo': book.titulo, 'Autor': book.autor, 'Genero': book.genero})
                return JsonResponse(allBooks, safe=False, status=200)
        return HttpResponse(status=404)
    else:
        return HttpResponse(status=405)

@csrf_exempt
def listGenderBooks(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        if data:
            gender = data['genero']
            books = BookDAO.getBooksByGender(gender)
            if books:
                allBooks = []
                for book in books:
                    allBooks.append({'Id': book.id, 'Titulo': book.titulo, 'Autor': book.autor, 'Genero': book.genero})
                return JsonResponse(allBooks, safe=False, status=200)
        return HttpResponse(status=404)
    else:
        return HttpResponse(status=405)



