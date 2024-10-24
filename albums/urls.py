from django.urls import path

from .views import *
urlpatterns=[

    path('albums/', album_list, name='album_list'),
    path('albums/<int:album_id>/', album_detail, name='album_detail'),
    path('albums/create/', album_create, name='album_create'),
    path('albums/update/<int:album_id>/', album_update, name='album_update'),
    path('albums/delete/<int:album_id>/', album_delete, name='album_delete'),
     path(
'albums/<int:album_id>/add_song/'
, add_song_to_album, name=
'add_song_to_album'
),  
    ]