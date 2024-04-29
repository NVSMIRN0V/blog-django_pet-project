from django.shortcuts import render


def login(request):
    return render(request, 'users/login.html', context={'title': 'Login'})


def register(request):
    return render(request, 'users/register.html', context={'title': 'Register'})
