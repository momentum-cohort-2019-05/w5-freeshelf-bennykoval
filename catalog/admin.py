from django.contrib import admin
from catalog.models import Book, Category, Favourite
# Register your models here.

admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Favourite)