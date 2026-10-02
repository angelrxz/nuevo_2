from django.contrib import admin

# Register your models here.

from .models import Libro

class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'fecha_publicacion', 'isbn', 'genero')
    search_fields = ('titulo', 'autor', 'isbn')
    list_filter = ('genero', 'fecha_publicacion')

admin.site.register(Libro, LibroAdmin)



    











