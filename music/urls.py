# /music/songs/ - List all songs

"""
/music/songs/<int:song_id>/ - View song details
/music/songs/create/ - Create a new song
/music/songs/update/<int:song_id>/ - Update a song
/music/songs/delete/<int:song_id>/ - Delete a song
/music/albums/ - List all albums
/music/albums/<int:album_id>/ - View album details
/music/albums/create/ - Create a new album
/music/albums/update/<int:album_id>/ - Update an album
/music/albums/delete/<int:album_id>/ - Delete an album
/music/genres/ - List all genres"""
# music/urls.py
from django.urls import path
from .views import (
    song_list,
    song_detail,
    song_create,
    song_update,
    song_delete,
    # album_list,
    # album_detail,
    # album_create,
    # album_update,
    # album_delete,
)

urlpatterns = [
    path('songs/', song_list, name='song_list'),
    path('songs/<int:song_id>/', song_detail, name='song_detail'),
    path('songs/create/', song_create, name='song_create'),
    path('songs/update/<int:song_id>/', song_update, name='song_update'),
    path('songs/delete/<int:song_id>/', song_delete, name='song_delete'),
    # path('albums/', album_list, name='album_list'),
    # path('albums/<int:album_id>/', album_detail, name='album_detail'),
    # path('albums/create/', album_create, name='album_create'),
    # path('albums/update/<int:album_id>/', album_update, name='album_update'),
    # path('albums/delete/<int:album_id>/', album_delete, name='album_delete'),
]
