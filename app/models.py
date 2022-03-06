from django.db import models
from .misc import *
from django.db.models.signals import post_save
from django.db.models.deletion import CASCADE

class UserManager(models.Manager):
    def validate(self, form):
        errors = {}
        usernameCheck - self.filter(username=form['username'])
        if usernameCheck:
            errors['username'] = 'Username already taken'
        if form['password'] != form['confirm']:
            errors['password'] = 'Passwords do not match'
        return errors

class User(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    permissions = models.IntegerField(default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    objects = UserManager()
    def __str__(self):
        return f'{self.firstName} {self.lastName}'

class Profile(models.Model):
    img = models.ImageField(upload_to='profileImgs', default='hive.jpg')
    user = models.OneToOneField(User, unique=True, on_delete=CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.user.firstName} {self.user.lastName} Profile'

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        User.objects.create(user=instance)
        post_save.connect(create_user_profile, sender=User)

class Status(models.Model):
    status = models.CharField(max_length=255)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    def __str__(self):
        return {self.status}

class Ownership(models.Model):
    ownership = models.CharField(max_length=255)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    def __str__(self):
        return {self.ownership}

class Genre(models.Model):
    genre = models.CharField(max_length=255)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    def __str__(self):
        return {self.genre}

class Author(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.firstName} {self.lastName}'

class Writer(models.Model):
    img = models.ImageField(upload_to='authorImgs', default='')
    author = models.OneToOneField(Author, unique=True, on_delete=CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.author.firstName} {self.author.lastName} Writer'

def create_author_writer(sender,  instance, created, **kwargs):
    if created:
        Author.objects.create(author=instance)
        post_save.connect(create_author_writer, sender=Author)

class Series(models.Model):
    name = models.CharField(max_length=255)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    def __str__(self):
        return {self.name}

class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name='bookUser', on_delete=CASCADE)
    status = models.ForeignKey(Status, related_name='bookStatus', on_delete=CASCADE, blank=True)
    ownership = models.ForeignKey(Ownership, related_name='bookOwnership', on_delete=CASCADE, blank=True)
    genre = models.ForeignKey(Genre, related_name='bookGenre', on_delete=CASCADE, blank=True)
    series = models.ForeignKey(Series, related_name='bookSeries', on_delete=CASCADE, blank=True)
    sequence = models.IntegerField(blank=True)
    author = models.ForeignKey(Author, related_name='bookAuthor', on_delete=CASCADE, blank=True)
    def __str__(self):
        return self.title

class Story(models.Model):
    img = models.ImageField(upload_to='bookImgs', default='hive.jpg')
    author = models.OneToOneField(Author, unique=True, on_delete=CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.book.title} Story'

def create_book_story(sender, instance, created, **kwargs):
    if created:
        Book.objects.create(book=instance)
        post_save.connect(create_book_story, sender=Book)