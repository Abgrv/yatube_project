from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def groups_posts(request):
    return HttpResponse('Список постов')
def index(request):
    return HttpResponse('Главная страница')
# Create your views here.
