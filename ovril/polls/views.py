from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Resenha

# Create your views here.
def login(request):
    return render(request, 'polls/login.html')

def register(request):
    return render(request, 'polls/register.html')

def index(request):
    resenhas_list = Resenha.objects.order_by('-data_publicacao')
    context = {'resenhas_list': resenhas_list}
    return render(request, 'polls/index.html', context)