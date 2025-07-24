from django.db import models
from django.utils import timezone


class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

#relación 1 a 1
class Datos_Aut(models.Model):
    autor = models.OneToOneField(Autor, on_delete=models.CASCADE, null=True, blank=True)
    identificacion = models.TextField(null=True, blank=True)
    fecha_nac = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.autor.nombre

#Relación muchos a muchos
class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autores = models.ManyToManyField(Autor, blank=True)
    fecha_publicacion = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return self.titulo
    
    def obtener_autores(self):
        return ", ".join([autor.nombre for autor in self.autores.all()])
    
    obtener_autores.short_description = 'Autores'


#Relación uno a muchos
class Resena(models.Model):
    resena = models.TextField()
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, null=True)
    fecha = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.libro.titulo
