'''This is the views'''
from django.shortcuts import render
from .models import Sobre

def inicio(request):
    '''This is the view of homepage'''
    contexto = Sobre.objects.all()
    return render(request, 'inicio.html', contexto)
