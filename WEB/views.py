from django.shortcuts import render

def Index(request):
    return render(request, 'index.html', {"title":"Главная | Acr Host"})