from django.shortcuts import get_object_or_404, render

# Create your views here.

from .models import Libro

def mostrar_libros(request):
    libros = Libro.objects.order_by('titulo')
    return render(request, 'libros.html', {'libros': libros})

def mostrar_libro_detalle(request, libro_id):
    libro = get_object_or_404(Libro, pk=libro_id)
    return render(request, 'libro_detalle.html', {'libro': libro})


