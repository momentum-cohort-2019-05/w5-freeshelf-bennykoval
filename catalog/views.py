from django.shortcuts import render, get_object_or_404
from catalog.models import Book, Category
from django.views import generic

# Create your views here.

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    books = Book.objects.all()
    
    context = {
        'books': books,   
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

# class CategoryDetailView(generic.DetailView):
#     model = Category

def list_books_by_category(request, category_pk):
    books_by_category = Book.objects.filter(categories__id=category_pk)
    category = get_object_or_404(Category, pk=category_pk)

    context = {
        'books_by_category': books_by_category,
        'category': category,
    }
    return render(request, 'category_book.html', context=context)
