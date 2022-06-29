from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница')

def group_posts(request):
    return HttpResponse('Список групп')

def group_posts_details(request, slug):
    return HttpResponse(f'Название группы ---> {slug}')
    