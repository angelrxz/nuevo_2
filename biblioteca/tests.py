from datetime import date

from django.test import TestCase
from django.urls import reverse

from .models import Libro


class LibroViewsTests(TestCase):
	def setUp(self):
		self.libro = Libro.objects.create(
			titulo='El principito',
			autor='Antoine de Saint-Exupery',
			fecha_publicacion=date(1943, 4, 6),
			isbn='9780156012195',
			genero='Fábula',
		)

	def test_mostrar_libros(self):
		response = self.client.get(reverse('mostrar_libros'))

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, self.libro.titulo)
		self.assertContains(response, reverse('mostrar_libro_detalle', args=[self.libro.pk]))

	def test_mostrar_libro_detalle(self):
		response = self.client.get(reverse('mostrar_libro_detalle', args=[self.libro.pk]))

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, self.libro.isbn)

	def test_libro_inexistente_devuelve_404(self):
		response = self.client.get(reverse('mostrar_libro_detalle', args=[0]))

		self.assertEqual(response.status_code, 404)
