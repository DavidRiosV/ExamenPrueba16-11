from django.urls import path,re_path
from.import views

urlpatterns = [
        path('',views.index,name='index'),
        path('videojuego/nombre',views.videojuego_fantasy,name='videojuego_fantasy'),
        path('videojuego/plataforma',views.plataforma_sony,name='plataforma_sony'),
        path('videojuego/sinplataforma',views.videojuego_sin_plataforma,name='videojuego_sin_plataforma'),
        path('videojuego/estudio/<str:estudio>',views.videojuegos_estudio,name='videojuegos_estudio'),
        path('videojuego/estudio/<str:c>/<str:f>/<str:p>',views.ultimo_analisis,name='ultimo_analisis')
]
