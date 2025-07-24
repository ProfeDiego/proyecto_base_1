from django.urls import path
from . import views
from .views import Biblioteca, ListaLibros, DetalleLibro, ListaAutores, AutorDetalle

app_name = 'apps.libro'

urlpatterns = [
    # path('libros/', views.lista_libros, name='libros'),
    path('libros/', Biblioteca.as_view(), name='biblioteca'),
    # path('lista_libros/', views.lista_libros, name='lista_libros'),
    path('lista_libros/', ListaLibros.as_view(), name='lista_libros'),
    # path('libros/<int:pk>/', views.detalle_libro, name='detalle_libro'),
    path('libros/<int:pk>/', DetalleLibro.as_view(), name='detalle_libro'),
    # path('autores/', views.lista_autores, name='lista_autores'),
    path('autores/', ListaAutores.as_view(), name='lista_autores'),
    # path('autores/<int:pk>/', views.detalle_autor, name='detalle_autor'),
    path('autores/<int:pk>/', AutorDetalle.as_view(), name='detalle_autor'),
]
