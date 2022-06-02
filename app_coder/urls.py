from unicodedata import name
from django.urls import path
from app_coder import views

urlpatterns = [
    path('/', views.inicio),
    path("cursos/", views.curso),
    path('profesores/', views.profesores),
    path('estudiantes/', views.estudiantes),
    path('entregables/', views.entregables),
]
