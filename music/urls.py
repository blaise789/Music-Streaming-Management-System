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
    
    path('', song_list, name='song_list'),
    path('songs/<int:song_id>/', song_detail, name='song_details'),
    path('songs/create/', song_create, name='song_create'),
    path('songs/update/<int:song_id>/', song_update, name='song_update'),
    path('songs/delete/<int:song_id>/', song_delete, name='song_delete'),
   
]
