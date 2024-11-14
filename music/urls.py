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
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('all_songs/', song_list, name='song_list'),
    path('songs/<int:song_id>/', song_detail, name='song_details'),
    path('songs/create/', song_create, name='song_create'),
    path('songs/update/<int:song_id>/', song_update, name='song_update'),
    path('songs/delete/<int:song_id>/', song_delete, name='song_delete'),
    path('play_song/<int:song_id>/', play_song_index, name='play_song_index'),
    path('songs/play/<int:song_id>/', play_song, name='song_play'),
    path('recent/', recent, name='recent'),
    path('rock_songs/', rock_songs, name='rock_songs'),
    path('play_recent_song/<int:song_id>/', play_recent_song, name='play_recent_song'),
    path('mymusic/', mymusic, name='mymusic'),
    


   
]
