from django.db import models

# Modelo para los géneros de los libros

class Genre(models.Model):
    """
    Modelo que representa un género literario (p. ej. ciencia ficción, poesía, etc.).
    """
    name = models.CharField(max_length=200, help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)")
    
    def __str__(self):
        """
        Cadena que representa a la instancia particular del modelo (p. ej en el sitio de Administración)
        """
        return self.name


# Modelo para los libros

from django.urls import reverse #Used to generate URLs by reversing the URL patterns

class Book(models.Model):
    """
    Modelo que representa un libro (pero no un Ejemplar específico).
    """

    title = models.CharField(max_length=200)

    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    # ForeignKey, ya que un libro tiene un solo autor, pero el mismo autor puede haber escrito muchos libros.
    # 'Author' es un string, en vez de un objeto, porque la clase Author aún no ha sido declarada.

    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
    
    isbn = models.CharField('ISBN',max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')

    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")
    # ManyToManyField, porque un género puede contener muchos libros y un libro puede cubrir varios géneros.
    # La clase Genre ya ha sido definida, entonces podemos especificar el objeto arriba.

    lenguaje = models.ForeignKey('Lenguaje', on_delete=models.SET_NULL, null=True)
    # Se agrega la relación con los lenguajes
    
    def __str__(self):
        """
        String que representa al objeto Book
        """
        return self.title
    
    
    def get_absolute_url(self):
        """
        Devuelve el URL a una instancia particular de Book
        """
        return reverse('book-detail', args=[str(self.id)])

    def display_genre(self):
        """
        Creates a string for the Genre. This is required to display genre in Admin.
        """
        return ', '.join([ genre.name for genre in self.genre.all()[:3] ])
    
    display_genre.short_description = 'Genre'


# Modelo de instancias de libros

import uuid # Requerida para las instancias de libros únicos
from django.contrib.auth.models import User # Para vincular las instancias con prestamos a usuarios
from datetime import date

class BookInstance(models.Model):
    """
    Modelo que representa una copia específica de un libro (i.e. que puede ser prestado por la biblioteca).
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID único para este libro particular en toda la biblioteca")
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True) 
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Disponibilidad del libro')

    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ["due_back"]
        

    def __str__(self):
        """
        String para representar el Objeto del Modelo
        """
        # return '%s (%s)' % (self.id,self.book.title) ->> esto funcionaba con python 2
        return '{0} ({1})'.format(self.book,self.id)
    
    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False


# Modelo para los autores

class Author(models.Model):
    """
    Modelo que representa un autor
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)
    
    def get_absolute_url(self):
        """
        Retorna la url para acceder a una instancia particular de un autor.
        """
        return reverse('author-detail', args=[str(self.id)])
    

    def __str__(self):
        """
        String para representar el Objeto Modelo
        """
        return '{0}, {1}'.format(self.last_name, self.first_name)


# Modelo para el lenguaje de los libros

class Lenguaje(models.Model):
    """
    Modelo que representa a un lenguaje
    """
    name = models.CharField('Lenguaje', max_length=50, help_text="Select a language for this book",)

    def __str__(self):
        """
        String que representa al objeto Book
        """
        return self.name
    