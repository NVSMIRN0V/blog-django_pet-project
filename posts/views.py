from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse(f'Page')
    # return render(request, '', context={'title': 'Главная'})


def create_post(request):
    return HttpResponse(f'Page')
    # return render(request, '', context={'title': 'Добавить'})


def detail_post(request):
    return HttpResponse(f'Page')
    # return render(request, '', context={'title': 'Пост'})


def post_list(request):
    return HttpResponse(f'Page')
    # return render(request, '', context={'title': 'Все посты'})
