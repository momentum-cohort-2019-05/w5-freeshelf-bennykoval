from django.shortcuts import render
from catalog.models import Book

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