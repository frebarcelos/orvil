from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from ..dao.UserDAO import UserDAO
from django.contrib.auth.hashers import make_password, check_password

@csrf_exempt
def createUser(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        if data:
            nome = data['nome']
            email = data['email']
            senha = data['senha']
            if UserDAO.getUserByEmail(email):
                return JsonResponse({'Error': 'Email already registered'}, safe=False, status=400)
            UserDAO.createUser(nome, email, senha)
            returnedData = {'Nome' : nome, 'Email' : email, 'Senha' : senha, 'Mensagem': 'Usuario criado com sucesso'}
            return JsonResponse(returnedData, safe=False, status=201)
    else:
        return HttpResponse(status=405)
@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        if data:
            email = data['email']
            password = data['senha']
            user = UserDAO.getUserByEmailAndPassowrd(email, password)
            if user:
                returnedData = {'Nome': user.nome, 'Email': user.email, 'Senha': user.senha,'Authorization': 'WIP'}
                return JsonResponse(returnedData, safe=False,status=200)
            return JsonResponse({'Error' : 'User not found'}, safe=False, status=404)
        return HttpResponse(status=400)
    else:
        return HttpResponse(status=405)

