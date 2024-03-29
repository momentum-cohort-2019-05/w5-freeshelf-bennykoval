"""freeshelf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from catalog import views
from catalog import models


urlpatterns = [
    path('', RedirectView.as_view(url='index/', permanent=True)),
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path ('category-books/<int:category_pk>', views.list_books_by_category, name='python'),
    path('accounts/', include('registration.backends.simple.urls')),
    path('favourite-book-list/', views.favourite_book_list, name='favourites'),
    path('new-favourite/<int:pk>/', views.favourite_book, name='favourite-book'),
]
