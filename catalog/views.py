from django.shortcuts import render

# Create your views here.

from .models import Book, Author, BookInstance, Genre

def index(request):
    """
    Función vista para la página inicio del sitio.
    """
    # Genera contadores de algunos de los objetos principales
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    # Libros disponibles (status = 'a')
    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_authors=Author.objects.count()  # El 'all()' esta implícito por defecto.
    num_generos=Genre.objects.count() # Para la cantidad total de géneros
    num_libros_esp=Book.objects.filter(lenguaje__name__exact='Castellano').count()
    
    # Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1


    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'index.html',
        context={
            'num_books':num_books,
            'num_instances':num_instances,
            'num_instances_available':num_instances_available,
            'num_authors':num_authors,
            'num_generos':num_generos,
            'num_libros_esp':num_libros_esp,
            'num_visits':num_visits
        },
    )

# Se crea una vista-de-clase, para eso en vez de una función se genera una clase por el modelo

from django.views import generic

class BookListView(generic.ListView):
    model = Book
    template_name = 'book_list.html'  # Specify your own template name/location
    paginate_by = 2

    def get_queryset(self):
        #return Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
        return Book.objects.all()
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(BookListView, self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context
        context['some_data'] = 'This is just some data'
        return context

class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author
    template_name = 'author_list.html'
    paginate_by = 2

    def get_queryset(self):
        return Author.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super(AuthorListView, self).get_context_data(**kwargs)
        return context

class AuthorDetailView(generic.DetailView):
    model = Author