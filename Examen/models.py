from django.db import models

# Create your models here.

class Estudio(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Sede(models.Model):
    pais = models.CharField(max_length=150)
    estudio = models.ForeignKey(Estudio, on_delete=models.CASCADE, related_name='sedes')

    def __str__(self):
        return f"{self.estudio.nombre} - {self.pais}"

class Plataforma(models.Model):
    nombre = models.CharField(max_length=150)
    fabricante = models.CharField(max_length=150)

    def __str__(self):
        return self.nombre

class Videojuego(models.Model):
    titulo = models.CharField(max_length=200)
    ventas_estimadas = models.IntegerField(null=True, blank=True)
    
    estudio_desarrollo = models.ForeignKey(Estudio, on_delete=models.CASCADE, related_name='videojuegos')
    plataformas = models.ManyToManyField(Plataforma, related_name='videojuegos', through='VideojuegoPlataforma')

    def __str__(self):
        return self.titulo

class VideojuegoPlataforma(models.Model):
    videojuego = models.ForeignKey(Videojuego, on_delete=models.CASCADE)
    plataforma = models.ForeignKey(Plataforma, on_delete=models.CASCADE)

class Critico(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Analisis(models.Model):
    puntuacion = models.IntegerField()
    fecha = models.DateField()
    
    videojuego = models.ForeignKey(Videojuego, on_delete=models.CASCADE, related_name='analisis')
    critico = models.ForeignKey(Critico, on_delete=models.CASCADE, related_name='analisis')

    def __str__(self):
        return f"{self.videojuego.titulo} - {self.puntuacion}"