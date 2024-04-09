from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('',views.login, name='login'),
    path('index',views.index, name='index'),
    path('register', views.register, name='register')
]