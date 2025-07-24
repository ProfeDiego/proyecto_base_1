from django.contrib import admin
from .models import Autor, Libro, Datos_Aut, Resena

admin.site.register(Autor)
admin.site.register(Datos_Aut)
admin.site.register(Resena)
@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'obtener_autores', 'fecha_publicacion', 'isbn')
    filter_horizontal = ('autores',)

