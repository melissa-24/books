from django.shortcuts import render, redirect
from django.contrib import messages
from ..models import *

# Landing pages
def theAdmin(request):
    if 'user_id' not in request.session:
        messages.error(request, "Protected Page")
        return redirect('/')
    else:
        user = User.objects.get(id=request.session['user_id'])
        users = User.objects.all().values()
        statuss = Status.objects.all().values().order_by('status')
        ownerships = Ownership.objects.all().values().order_by('ownership')
        genres = Genre.objects.all().values().order_by('genre')
        authors = Author.objects.all().values().order_by('lastName')
        seriess = Series.objects.all().values().order_by('name')
        books = Book.objects.all().values().order_by('title')
        context = {
            'user': user,
            'users': users,
            'statuss': statuss,
            'ownerships': ownerships,
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

def users(request):
    if 'user_id' not in request.session:
        messages.error(request, 'Protected Page')
        return redirect('/')
    else:
        user = User.objects.get(id=request.session['user_id'])
        users = User.objects.all().values().order_by('lastName')
        context = {
            'user': user,
            'users': users,
        }
        return render(request, 'logged/admin/user.html')

def adminBooks(request):
    if 'user_id' not in request.session:
        messages.error(request, "Protected Page")
        return redirect('/')
    else:
        user = User.objects.get(id=request.session['user_id'])
        books = Book.objects.all().values().order_by('title')
        context = {
            'user': user,
            'books': books,
        }
        return render(request, 'logged/admin/book.html', context)

def adminAuthors(request):
    if 'user_id' not in request.session:
        messages.error(request, "Protected Page")
        return redirect('/')
    else:
        user = User.objects.get(id=request.session['user_id'])
        authors = Author.objects.all().values().order_by('lastName')
        context = {
            'user': user,
            'authors': authors,
        }
        return render(request, 'logged/admin/author.html', context)

# Create 
def createStatus(request):
    Status.objects.create(
        status = request.POST['status']
    )
    messages.error(request, 'Status created')
    return redirect('/theAdmin/')

def createOwnership(request):
    Ownership.objects.create(
        ownership = request.POST['ownership']
    )
    messages.error(request, 'Ownership created')
    return redirect('/theAdmin/')

def createGenre(request):
    Genre.objects.create(
        genre = request.POST['genre']
    )
    messages.error(request, 'Genre created')
    return redirect('/theAdmin/')

def createAuthor(request):
    Author.objects.create(
        firstName = request.POST['firstName'],
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
        ownership_id = request.POST['ownership'],
        genre_id = request.POST['genre'],
        series_id = request.POST['series'],
        sequence = request.POST['sequence'],
        author_id = request.POST['author']
    )
    messages.error(request, 'Book created')
    return redirect('/theAdmin/')

# Update
def updateProfile(request, user_id):
    toUpdate = User.objects.get(id=user_id)
    toUpdate.profile.img = request.FILES['img']
    toUpdate.save()
    messages.error(request, 'User Profile Images updated')
    return redirect('/theAdmin/users/')
    
def updateUser(request, user_id):
    toUpdate = User.objects.get(id=user_id)
    toUpdate.firstName = request.POST['firstName']
    toUpdate.lastName = request.POST['lastName']
    toUpdate.save()
    messages.error(request, 'User updated')
    return redirect('/theAdmin/users/')

def updateAdmin(request, user_id):
    toUpdate = User.objects.get(id=user_id)
    toUpdate.permissions = 24
    toUpdate.save()
    messages.error(request, 'User permissions changed to Admin')
    return redirect('/theAdmin/user/')

def updatePermission(request, user_id):
    toUpdate = User.objects.get(id=user_id)
    toUpdate.permissions = 1
    toUpdate.save()
    messages.error(request, 'User permissions changed to Contributor')
    return redirect('/theAdmin/users/')

def updateStatus(request, status_id):
    toUpdate = Status.objects.get(id=status_id)
    toUpdate.status = request.POST['status']
    toUpdate.save()
    messages.error(request, "Status Updated")
    return redirect('/theAdmin/')

def updateOwnership(request, ownership_id):
    toUpdate = Ownership.objects.get(id=ownership_id)
    toUpdate.ownership = request.POST['ownership']
    toUpdate.save()
    messages.error(request, "Ownership updated")
    return redirect('/theAdmin/')

def updateGenre(request, genre_id):
    toUpdate = Genre.objects.get(id=genre_id)
    toUpdate.genre = request.POST['genre']
    toUpdate.save()
    messages.error(request, "Genre updated")
    return redirect('/theAdmin/')

def updateAuthor(request, author_id):
    toUpdate = Author.objects.get(id=author_id)
    toUpdate.firstName = request.POST['firstName']
    toUpdate.lastName = request.POST['lastName']
    toUpdate.save()
    messages.error(request, "Author updated")
    return redirect('/theAdmin/authors/')

def updateWriter(request, author_id):
    toUpdate = Author.objects.get(id=author_id)
    toUpdate.writer.img = request.FILES['img']
    toUpdate.save()
    messages.error(request, "Author Image updated")
    return redirect('/theAdmin/authors/')

def updateSeries(request, series_id):
    toUpdate = Series.objects.get(id=series_id)
    toUpdate.series = request.POST['series']
    toUpdate.save()
    messages.error(request, "Series updated")
    return redirect('/theAdmin/')

def updateBook(request, book_id):
    toUpdate = Book.objects.get(id=book_id)
    toUpdate.title = request.POST['title']
    toUpdate.description = request.POST['description']
    toUpdate.save()
    messages.error(request, "Book updated")
    return redirect('/theAdmin/books/')

def updateBookStatus(request, book_id):
    toUpdate = Book.objects.get(id=book_id)
    toUpdate.status_id = request.POST['status']
    toUpdate.save()
    messages.error(request, "Status was updated")
    return redirect('/theAdmin/books/')

def updateBookOwnership(request, book_id):
    toUpdate = Book.objects.get(id=book_id)
    toUpdate.ownership_id = request.POST['ownership']
    toUpdate.save()
    messages.error(request, "Status was updated")
    return redirect('/theAdmin/books/')

def updateStory(request, book_id):
    toUpdate = Book.objects.get(id=book_id)
    toUpdate.story.img = request.FILES['img']
    toUpdate.save()
    messages.error(request, "Book Image updated")
    return redirect('/theAdmin/books/')


# Delete
def deleteStatus(request, status_id):
    toDelete = Status.objects.get(id=status_id)
    toDelete.delete()
    messages.error(request, 'Status Deleted')
    return redirect('/theAdmin/')

def deleteOwnership(request, ownership_id):
    toDelete = Ownership.objects.get(id=ownership_id)
    toDelete.delete()
    messages.error(request, 'Ownership Deleted')
    return redirect('/theAdmin/')

def deleteGenre(request, genre_id):
    toDelete = Genre.objects.get(id=genre_id)
    toDelete.delete()
    messages.error(request, 'Genre Deleted')
    return redirect('/theAdmin/')

def deleteAuthor(request, author_id):
    toDelete = Author.objects.get(id=author_id)
    toDelete.delete()
    messages.error(request, 'Author Deleted')
    return redirect('/theAdmin/')

def deleteSeries(request, series_id):
    toDelete = Series.objects.get(id=series_id)
    toDelete.delete()
    messages.error(request, 'Series Deleted')
    return redirect('/theAdmin/')

def deleteBook(request, book_id):
    toDelete = Book.objects.get(id=book_id)
    toDelete.delete()
    messages.error(request, 'Book Deleted')
    return redirect('/theAdmin/')