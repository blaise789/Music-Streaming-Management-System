from django.urls import path
from .views import PlaylistListView, PlaylistDetailView, PlaylistCreateView, PlaylistEditView, PlaylistDeleteView

urlpatterns = [
    path('playlists/', PlaylistListView.as_view(), name='playlist_list'),
    path('playlists/<int:pk>/', PlaylistDetailView.as_view(), name='playlist_detail'),
    path('playlists/create/', PlaylistCreateView.as_view(), name='playlist_create'),
    path('playlists/edit/<int:pk>/', PlaylistEditView.as_view(), name='playlist_edit'),
    path('playlists/delete/<int:pk>/', PlaylistDeleteView.as_view(), name='playlist_delete'),
]
