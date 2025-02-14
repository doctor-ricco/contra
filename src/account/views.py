from django.shortcuts import render

from  django.http import HttpRequest, HttpResponse

async def home(request: HttpRequest) -> HttpResponse:
    #return HttpResponse("Estamos na home da app de account")
    #return render(request, 'account/home.html')
    return render(request, 'account/home.html', { 'x' : 33 }) #Fazendo o rendering da home e passando um parâmetro pra dentro dela como um dicionário 


async def register(request: HttpRequest) -> HttpResponse:
    #return HttpResponse("Estamos na register da app de account")
    return render(request, 'account/register.html')


async def login(request: HttpRequest) -> HttpResponse:
    #return HttpResponse("Estamos na login da app de account")
    return render(request, 'account/login.html')

