from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name

    def get_absolute_url(self):
        return reverse('category-books', args=[str(self.id)])

class Book(models.Model):
    """Model representing a book."""
    title = models.CharField(max_length=200, help_text='Enter the title of the book')
    author = models.CharField(max_length=200, help_text='Enter the author of the book')
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    category = models.ManyToManyField(Category)
    timestamp = models.DateField(default=date.today)
    url = models.URLField(unique=True)
    image_url = models.URLField(null=True)

    user = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        """String for representing the Model object."""
        return self.title

# class Category(models.Model):
#     """Model representing a category."""

#     BOOK_CATEGORY = ['Python', 'Django', 'JavaScript', 'Lua',]

# class Favourites(models.Model):
#     """Model representing user favourites."""
#     owner = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True)
#     favourite = models.BooleanField()