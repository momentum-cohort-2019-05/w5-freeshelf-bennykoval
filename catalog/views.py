from django.shortcuts import render, get_object_or_404
from catalog.models import Book, Category, Favourite
from django.views import generic
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    books = Book.objects.all()
    favourites = []
    if not request.user.is_anonymous:
        for fav in Favourite.objects.filter(user=request.user):
            favourites.append(fav.book)
        
    context = {
        'books': books,
        'favourites': favourites,
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

@login_required
def favourite_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    existing_favourites = Favourite.objects.filter(user=request.user,book=book)
    print(existing_favourites)
    if existing_favourites.count() > 0:
        existing_favourites.delete()
    else:
        newFav = Favourite(
            user=request.user,
            book=book
        )
        newFav.save()
    return HttpResponseRedirect(request.GET.get("next"))

@login_required
def favourite_book_list(request):
    favourites = Favourite.objects.filter(user=request.user)
    context = {
        'favourites': favourites,
    }

    return render(request, 'favourites.html', context=context)
