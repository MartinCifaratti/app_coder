import http
from http.client import HTTPResponse
from django.shortcuts import render

# Create your views here.

def inicio(request):
    return HTTPResponse("vista inicio")

def curso(request):
    return HTTPResponse("vista cursos")

def profesores(request):
    return HTTPResponse("vista profesores")

def estudiantes(request):
    return HTTPResponse("vista estudiantes")

def entregables(request):
    return HTTPResponse("vista entregables")