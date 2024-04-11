from django.urls import path
from ..view.UserView import createUser, login

urlpatterns = [
    path('cadastrar/', createUser, name='createUser'),
    path('login/', login, name='login'),
]