from django.shortcuts import render
from django.http import HttpResponse

#from AppCoder.models import Curso

def inicio(request):
    return HttpResponse('vista de inicio')

def cursos(request):
    return HttpResponse('vista de cursos')

def profesores(request):
    return HttpResponse('vista de profesores')

def estudiantes(request):
    return HttpResponse('vista de estudiantes')

def entregables(request):
    return HttpResponse('vista de entregables')
