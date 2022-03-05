from django.shortcuts import render, redirect
from django.contrib import messaes
from ..models import *

def theAdmin(request):
    if 'user_id' not in request.session:
        messages.error(request, "Protected Page")
        return redirect('/')
    else:
        user = User.objects.get(id=request.session['user_id'])
        users = User.objects.all().values()
        statuss = Status.objects.all().values().order_by('status')
        genres = Genre.objects.all().values().order_by('genre')
        authors = Author.objects.all().values().order_by('lastName')
        seriess = Series.objects.all().values().order_by('name')
        books = Book.objects.all().values().order_by('title')
        context = {
            'user': user,
            'users': users,
            'statuss': statuss,
            'genres': genres,
            'authors': authors,
            'seriess': seriess,
            'books': books,
        }
        return render(request, 'logged/admin/theAdmin.html', context)

def profile(request, user_id):
    if 'user_id' not in request.session:
        messages.error(request, 'Protected Page')
        return redirect('/')
    else:
        user = User.objects.get(id=user_id)
        theUser = User.objects.get(id=request.session['user_id'])
        context = {
            'user': user,
            'theUser': theUser,
        }
        return render(request, 'logged/admin/profile.html', context)

def createStatus(request):
    Status.objects.create(
        status = request.POST['status']
    )
    messages.error(request, 'Status created')
    return redirect('/theAdmin/')

def createGenre(request):
    Genre.objects.create(
        genre = request.POST['genre']
    )
    messages.error(request, 'Genre created')
    return redirect('/theAdmin/')

def createAuthor(request):
    Author.objects.create(
        firstName = request.POST['fistName'],
        lastName = request.POST['lastName'],
    )
    messages.error(request, 'Author created')
    return redirect('/theAdmin/')

def createSeries(request):
    Series.objects.create(
        name = request.POST['name']
    )
    messages.error(request, 'Series created')
    return redirect('/theAdmin/')

def createBook(request):
    Book.objects.create(
        title = request.POST['title'],
        description = request.POST['description'],
        user_id = request.POST['user'],
        status_id = request.POST['status'],
        genre_id = request.POST['genre'],
        series_id = request.POST['series'],
        sequence = request.POST['sequence'],
        author_id = request.POST['author']
    )
    messages.error(request, 'Book created')
    return redirect('/theAdmin/')