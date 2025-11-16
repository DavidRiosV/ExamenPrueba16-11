from django.shortcuts import render
from .models import Videojuego,Estudio,Plataforma,VideojuegoPlataforma,Analisis,Sede,Critico
from django.db.models import Q,Prefetch,Sum

def index(request):
    return render(request, 'Examen/index.html')

def videojuego_fantasy(request):
    videojuegos=Videojuego.objects.filter(titulo__contains="fantasy",estudio_desarrollo__sedes__pais__icontains='Unidos').select_related("estudio_desarrollo").prefetch_related("plataformas","analisis").all()

    return render(request,'Examen/videojuego_fantasy.html',{'videojuegos': videojuegos})


def mi_error_404(request,exception=None):
    return render(request, 'Errores/404.html',None,None,404)

def mi_error_400(request, exception=None):
    return render(request, 'errors/400.html', None,None,400)

def mi_error_403(request, exception=None):
    return render(request, 'errors/403.html', None,None,403)

def mi_error_500(request):
    return render(request, 'errors/500.html', None,None,500)