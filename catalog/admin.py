from django.contrib import admin
from catalog.models import Book
from catalog.models import Category
# Register your models here.

admin.site.register(Book)
admin.site.register(Category)