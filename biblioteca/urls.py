from django.urls import path
from .views import mostrar_libros, mostrar_libro_detalle

urlpatterns = [
    path('', mostrar_libros, name='mostrar_libros'),
    path('<int:libro_id>/', mostrar_libro_detalle, name='mostrar_libro_detalle'),
]

