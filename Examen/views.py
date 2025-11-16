from django.shortcuts import render
from .models import Videojuego,Estudio,Plataforma,VideojuegoPlataforma,Analisis,Sede,Critico
from django.db.models import Q,Prefetch,Sum

def index(request):
    return render(request, 'Examen/index.html')

#Ejercicio 1
def videojuego_fantasy(request):
    videojuegos=Videojuego.objects.filter(titulo__contains="fantasy",estudio_desarrollo__sedes__pais__icontains='Unidos').select_related("estudio_desarrollo").prefetch_related("plataformas","analisis").all()

    return render(request,'Examen/videojuego_fantasy.html',{'videojuegos': videojuegos})

#Ejercicio 2
def plataforma_sony(request):
    videojuegos=Videojuego.objects.filter(Q(plataformas__fabricante__contains='Sony')|Q(plataformas__nombre__contains='Play Station'),analisis__puntuacion__gt=75).select_related("estudio_desarrollo").prefetch_related("plataformas","analisis").distinct()[:3]

    return render(request,'Examen/plataforma_sony.html',{'videojuegos': videojuegos})

#Ejercicio 3
def videojuego_sin_plataforma(request):
    videojuegos=Videojuego.objects.filter(plataformas__isnull=True).select_related("estudio_desarrollo").prefetch_related("analisis","plataformas").order_by('-ventas_estimadas').all()

    return render(request,'Examen/videojuego_sin_plataforma.html',{'videojuegos': videojuegos})

#Ejercicio 4 sin optimizar (uso del prefetch)
def estudios(request,año,):
    estudios=Estudio.objects.filter(videojuegos__analisis__fecha__year=año).order_by('-max_puntuacion').distinct()

    return render(request,'Examen/estudios.html',{'estudios': estudios})

#Ejercicio 5 videojuego con estuidio concreto y puntuacion de mayor de 7.5
def videojuegos_estudio(request,estudio):
    videojuegos=Videojuego.objects.filter(estudio_desarrollo__nombre=estudio,analisis__puntuacion__gt=7.5).select_related("estudio_desarrollo").prefetch_related("analisis","plataformas").order_by('-ventas_estimadas').distinct()

    return render(request,'Examen/videojuegos_estudio.html',{'videojuegos': videojuegos})

#Ejercicio 6 critico fabricante y plataforma que le pase

def ultimo_analisis(request,c,f,p):
    analisis = (
    Analisis.objects
    .filter(
        critico__nombre=c,
        videojuego__plataformas__fabricante=f,
        videojuego__estudio_desarrollo__sedes__pais=p,
    )
    .select_related('videojuego', 'critico')
    .prefetch_related('videojuego__plataformas', 'videojuego__estudio_desarrollo__sedes')
    .order_by('-fecha')   
    .distinct()           
    .first()              
)

    return render(request,'Examen/ultimo_analisis.html',{'analisis': analisis})

#Errores
def mi_error_404(request,exception=None):
    return render(request, 'Errores/404.html',None,None,404)

def mi_error_400(request, exception=None):
    return render(request, 'errors/400.html', None,None,400)

def mi_error_403(request, exception=None):
    return render(request, 'errors/403.html', None,None,403)

def mi_error_500(request):
    return render(request, 'errors/500.html', None,None,500)