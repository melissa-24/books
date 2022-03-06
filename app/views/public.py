from django.shortcuts import render, redirect
from django.contrib import messages
from ..models import *

def index(request):
    genre = Genre.objects.all().count()
    author = Author.objects.all().count()
    series = Series.objects.all().count()
    book = Book.objects.all().count()
    if 'user_id' not in request.session:
        context = {
            'genre': genre,
            'author': author,
            'series': series,
            'book': book,
        }
        return render(request, 'index.html', context)
    else:
        user = User.objects.get(id=request.session['user_id'])
        context = {
            'user': user,
            'genre': genre,
            'author': author,
            'series': series,
            'book': book,
        }
        return render(request, 'logged/index.html', context)

def genre(request):
    genres = Genre.objects.all().values()
    books = Book.objects.all().values()
    if 'user_id' not in request.session:
        context = {
            'genres': genres,
            'books': books,
        }
        return render(request, 'genre.html', context)
    else:
        user = User.objects.get(id=request.session['user_id'])
        context = {
            'user': user,
            'genres': genres,
            'books': books,
        }
        return render(request, 'logged/genre.html', context)

def viewGenre(request, genre_id):
    genre = Genre.objects.get(id=genre.id)
    books = Book.objects.all().values()
    if 'user_id' not in request.session:
        context = {
            'genre': genre,
            'books': books
        }
        return render(request, 'views/viewGenre.html', context)
    else:
        user = User.objects.get(id=request.session['user_id'])
        context = {
            'user': user,
            'genre': genre,
            'books': books
        }
        return render(request, 'logged/views/viewGenre.html', context)

def series(request):
    seriess = Series.objects.all().values().order_by('name')
    books = Book.objects.all().values().order_by('title')
    if 'user_id' not in request.session:
        context = {
            'seriess': seriess,
            'books': books,
        }
        return render(request, 'series.html', context)
    else:
        user = User.objects.get(id=request.session['user_id'])
        context = {
            'seriess': seriess,
            'books': books,
        }
        return render(request, 'logged/series.html', context)

def viewSeries(request, series_id):
    series = Series.objects.get(id=series_id)
    books = Books.objects.all().values().order_by('title')
    if 'user_id' not in request.session:
        context = {
            'series': series,
            'books': books,
        }
        return render(request, 'views/viewSeries.html', context)
    else:
        user = User.objects.get(id=request.session['user_id'])
        context = {
            'user': user,
            'series': series,
            'books': books,
        }
        return render(request, 'logged/views/viewSeries.html', context)

def author(request):
    authors = Author.objects.all().values().order_by('lastName')
    books = Book.objects.all().values()
    if 'user_id' not in request.session:
        context = {
            'authors': authors,
            'books': books,
        }
        return render(request, 'author.html', context)
    else:
        user = User.objects.get(id=request.session['user_id'])
        context = {
            'user': user,
            'authors': authors,
            'books': books,
        }
        return render(request, 'logged/author.html', context)

def viewAuthor(request, author_id):
    author = Author.objects.get(id=author_id)
    books = Book.objects.all().values().order_by('title')
    if 'user_id' not in request.session:
        context = {
            'author': author,
            'books': books,
        }
        return render(request, 'views/viewAuthor.html', context)
    else:
        user = User.objects.get(id=request.session['user_id'])
        context = {
            'user': user,
            'author': author,
            'books': books,
        }
        return render(request, 'logged/views/viewAuthor.html', context)

def books(request):
    books = Book.objects.all().values().order_by('title')
    authors = Author.objects.all().values()
    seriess = Series.objects.all().values()
    genres = Genre.objects.all().values()
    if 'user_id' not in request.session:
        context = {
            'books': books,
            'authors': authors,
            'seriess': seriess,
            'genres': genres,
        }
        return render(request, 'book.html', context)
    else:
        user = User.objects.get(id=request.session['user_id'])
        context = {
            'user': user,
            'books': books,
            'authors': authors,
            'seriess': seriess,
            'genres': genres,
        }
        return render(request, 'logged/book.html', context)

def viewBook(request, book_id):
    book = Book.objects.get(id=book_id)
    authors = Author.objects.all().values()
    seriess = Series.objects.all().values()
    genres = Genre.objects.all().values()
    statuses = Status.objects.all().values()
    ownerships = Ownership.objects.all().values()
    if 'user_id' not in request.session:
        context = {
            'book': book,
            'authors': authors,
            'seriess': seriess,
            'genres': genres,
            'statuses': statuses,
            'ownerships': ownerships,
        }
        return render(request, 'views/viewBook.html', context)
    else:
        user = User.objects.get(id=request.session['user_id'])
        context = {
            'user': user,
            'book': book,
            'authors': authors,
            'seriess': seriess,
            'genres': genres,
            'statuses': statuses,
            'ownerships': ownerships,
        }
        return render(request, 'logged/views/viewBook.html', context)