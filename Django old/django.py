#django is frontend and not secure
#views.py
from django.shortcuts import render
from .models import Book

def index(request):
    books = Book.objects.all()
    return render(request, 'reading/index.html', {'books': books})

def info(request, book_id):
    book = Book.objects.get(pk=book_id)
    return render(request, 'reading/info.html', {'book': book})

#info.html
{{book}}

#index.html
# <ul>
#     {% for book in books %}
#     <li><a href="{% url 'reading:info' book.id%}">{{book.title}}</a></li>
#     {% endfor %}
# </ul>


#urls.py
from django.urls import path

from . import views

app_name ="reading"

urlpatterns = [
    path('', views.index, name='index'),
    path('test/<int:book_id>', views.info, name='info')
]

#models.py
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    pages = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.title} is {self.pages} long"