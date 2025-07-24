from django.shortcuts import render
from django.views.generic import DetailView, TemplateView, ListView
from .models import Libro, Autor, Datos_Aut, Resena
from django.shortcuts import render, get_object_or_404
from .forms import ResenaForm
from django.urls import reverse_lazy
from django.views.generic.edit import FormMixin


''' 
Lista de Autores y Libros
'''
#vista basada en funciones
# def libros(request):
#     return render(request, 'libros/biblioteca.html')

#vista basada en clases
class Biblioteca(TemplateView):
    template_name = 'libros/biblioteca.html'



''' 
Lista de Libros
'''
#vista basada en funciones
# def lista_libros(request):
#     libros = Libro.objects.all().order_by('titulo')
#     context = {
#         'libros': libros
#     }
#     return render(request, 'libros/lista_libros.html', context)

#vista basada en clases
class ListaLibros(ListView):
    model = Libro
    template_name = 'libros/lista_libros.html'
    context_object_name = 'libros' # Por defecto, ListView usa 'object_list' o el nombre del modelo en plural ('libro_list').
    ordering = ['titulo']          # Equivalente a .order_by('titulo')



''' 
Detalle de Libro
'''
#vista basada en funciones
# def detalle_libro(request, pk):
#     libro = get_object_or_404(Libro, pk=pk)
#     context = {
#         'libro': libro
#     }
#     return render(request, 'libros/detalle_libro.html', context)

#vista basada en clases
class DetalleLibro(FormMixin, DetailView):
    model = Libro
    template_name = 'libros/detalle_libro.html'
    context_object_name = 'libro'

    form_class = ResenaForm


    # Método para pasar el formulario y las reseñas existentes al contexto
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Obtiene el libro actual que se está mostrando
        libro = self.get_object() 
        
        # Pasa todas las reseñas asociadas a este libro al contexto
        # Django crea automáticamente un related_name inverso 'resena_set'
        # si no se especifica 'related_name' en la ForeignKey.
        context['resenas'] = libro.resena_set.all().order_by('-id') # Ordenar por las más recientes
        
        # Pasa una instancia del formulario de reseña al contexto
        context['form'] = self.get_form() 
        return context

    # Método para manejar las solicitudes POST (cuando se envía el formulario)
    def post(self, request, *args, **kwargs):
        self.object = self.get_object() # Obtiene el libro al que se le está añadiendo la reseña
        form = self.get_form() # Obtiene una instancia del formulario con los datos enviados

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    # Método que se ejecuta si el formulario es válido
    def form_valid(self, form):
        # Asigna el libro actual a la reseña antes de guardarla
        resena = form.save(commit=False)
        resena.libro = self.object # 'self.object' es el Libro que estamos viendo
        resena.save()
        # Redirige a la misma página de detalle del libro después de guardar la reseña
        return super().form_valid(form)

    # Método para definir a dónde redirigir después de un envío exitoso del formulario
    def get_success_url(self):
        # Redirige a la misma URL de detalle del libro, usando el PK del libro actual
        return reverse_lazy('apps.libro:detalle_libro', kwargs={'pk': self.object.pk})



'''
Vista para autores
Lista de autores
'''

#vista basada en funciones
# def lista_autores(request):
#     autores = Autor.objects.all().order_by('nombre')
#     context = {
#         'autores': autores
#     }
#     return render(request, 'libros/lista_autores.html', context)

#vista basada en clases
class ListaAutores(ListView):
    model = Autor
    template_name = 'libros/lista_autores.html'
    context_object_name = 'autores' 
    ordering = ['nombre']  


''' 
Detalle de Autores
'''
# vista basada en funciones
# def detalle_autor(request, pk):
#     autor = get_object_or_404(Autor, pk=pk)
#     context = {
#         'autor': autor,
#     }
#     return render(request, 'libros/detalle_autor.html', context)
# ----------------------------
# vista basada en clases CBV (Class Based Views - CBVs)
class AutorDetalle(DetailView):
    model = Autor
    template_name = 'libros/detalle_autor.html'
    # Opcional: Define el nombre del objeto en el contexto para la plantilla.
    # Por defecto, DetailView usa 'object' o el nombre del modelo en minúsculas ('autor' en este caso).
    # Aquí lo dejamos explícito, aunque 'autor' sería el default.
    context_object_name = 'autor' 
