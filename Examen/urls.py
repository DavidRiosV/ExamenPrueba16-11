from django.urls import path,re_path
from.import views

urlpatterns = [
        path('',views.index,name='index'),
        path('videojuego/lista',views.videojuego_fantasy,name='videojuego_fantasy')
]
