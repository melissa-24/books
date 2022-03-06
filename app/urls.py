from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Main
    path('', views.index),
    path('logReg/', views.logReg),
    path('logout/', views.logout),
    path('register/', views.register),
    path('login/', views.login),
    # Main/Genre
    path('genre/', views.genre),
    path('genre/<int:genre_id>/view/', views.viewGenre),
    # Main/Series
    path('series/', views.series),
    path('series/<int:series_id>/view/', views.viewSeries),
    # Main/Author
    path('author/', views.author),
    path('author/<int:author_id>/view/', views.viewAuthor),
    # Main/Book
    path('book/', views.books),
    path('book/<int:book_id>/view/', views.viewBook),
    # Admin
    path('theAdmin/', views.theAdmin),
    # Admin/User
    path('theAdmin/user/', views.users),
    path('theAdmin/user/<int:user_id>/update/', views.updateUser),
    path('theAdmin/user/<int:user_id>/admin/update/', views.updateAdmin),
    path('theAdmin/user/<int:user_id>/permission/update/', views.updatePermission),
    path('theAdmin/user/<int:user_id>/view/', views.profile),
    path('theAdmin/user/<int:user_id>/profile/update/', views.updateProfile),
    # Admin/Book
    path('theAdmin/book/', views.adminBooks),
    path('theAdmin/book/create/', views.createBook),
    path('theAdmin/book/<int:book_id>/update/', views.updateBook),
    path('theAdmin/book/<int:book_id>/status/update/', views.updateBookStatus),
    path('theAdmin/book/<int:book_id>/ownership/update/', views.updateBookOwnership),
    path('theAdmin/book/<int:book_id>/delete/', views.deleteBook),
    path('theAdmin/book/story/<int:book_id>/update/', views.updateStory),
    # Admin/Author
    path('theAdmin/author/', views.adminAuthors),
    path('theAdmin/author/create/', views.createAuthor),
    path('theAdmin/author/<int:author_id>/update/', views.updateAuthor),
    path('theAdmin/author/<int:author_id>/delete/', views.deleteAuthor),
    path('theAdmin/author/writer/<int:author_id>/update/', views.updateWriter),
    # Admin/Status
    path('theAdmin/status/create/', views.createStatus),
    path('theAdmin/status/<int:status_id/update/', views.updateStatus),
    path('theAdmin/status/<int:status_id>/delete/', views.deleteStatus),
    # Admin/Ownership
    path('theAdmin/ownership/create/', views.createOwnership),
    path('theAdmin/ownership/<int:ownership_id>/update/', views.updateOwnership),
    path('theAdmin/ownership/<int:ownership_id>/delete/', views.deleteOwnership),
    # Admin/Genre
    path('theAdmin/genre/create/', views.createGenre),
    path('theAdmin/genre/<int:genre_id>/update/', views.updateGenre),
    path('theAdmin/genre/<int:genre_id>/delete/', views.deleteGenre),
    # Admin/Series
    path('theAdmin/series/create/', views.createSeries),
    path('theAdmin/series/<int:series_id>/update/', views.updateSeries),
    path('theAdmin/series/<int:series_id>/delete/', views.deleteSeries),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
