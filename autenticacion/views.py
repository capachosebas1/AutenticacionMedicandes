from django.http import HttpResponse
from django.shortcuts import render

def healthCheck(request):
        return HttpResponse('ok')

def home(request):
    return HttpResponse("Bienvenido a Medicandes")

def index(request):
    return render(request, 'index.html')