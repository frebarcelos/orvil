from backend.model.BookModel import Book

class BookDAO():

    @staticmethod
    def createBook(titulo,autor,genero):
        try:
            Book.objects.create(titulo=titulo,autor=autor,genero=genero)
        except Exception as e:
            print(e)


    @staticmethod
    def getBookById(id):
        try:
            return Book.objects.get(id=id)
        except:
            return None

    @staticmethod
    def getBooksByAuthor(autor):
        try:
            return Book.objects.filter(autor=autor)
        except:
            return None

    @staticmethod
    def getBooksByGender(genero):
        try:
            return Book.objects.filter(genero=genero)
        except:
            return None

    @staticmethod
    def getAllBooks():
        try:
            return Book.objects.all()
        except:
            return None

    @staticmethod
    def getBookByTitle(titulo):
        try:
            return Book.objects.get(titulo=titulo)
        except:
            return None

    @staticmethod
    def updateBook(id, titulo, autor, genero):
        book = BookDAO.getBookById(id)
        if book:
            if titulo:
                book.titulo = titulo
            if autor:
                book.autor = autor
            if genero:
                book.genero = genero
            book.save()
            return book
        return None

    @staticmethod
    def deleteBook(id):
        book = BookDAO.getBookById(id)
        if book:
            book.delete()
            return True
        return False






