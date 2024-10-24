# views.py
from datetime import timedelta
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
# import message
from django.contrib import messages
from playlists.models import Playlist
from .models import Song
# , Album
from .forms import SongForm
from mutagen import File  

@login_required
def song_create(request):
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            song = form.save(commit=False)
            audio_file = request.FILES['audio_file']
            audio = File(audio_file)
            duration = audio.info.length  
            song.duration = timedelta(seconds=duration)
            song.save()
            return redirect('song_list')
    else:
        form = SongForm()
    return render(request, 'song_form.html', {'form': form})

def song_list(request):
    songs = Song.objects.all()
    return render(request, 'songs_list.html', {'songs': songs})
def song_detail(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    playlists=Playlist.objects.filter(user=request.user) 
    if request.method == 'POST':
        playlist_name=request.POST.get('playlist')
        playlist=Playlist.objects.get(name=playlist_name,user=request.user)
        playlist.songs.add(song)
        messages.success(request,f'Song "{song.title}" has been added to "{playlist.name}".')
    return render(request, 'song_details.html', {'song': song,'playlists': playlists})



@login_required
def song_update(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES, instance=song)
        if form.is_valid():
            form.save()
            return redirect('song_list')
    else:
        form = SongForm(instance=song)
    return render(request, 'song_form.html', {'form': form})

@login_required
def song_delete(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    if request.method == 'POST':
        song.delete()
        return redirect('song_list')
    return render(request, 'song_confirm_delete.html', {'song': song})
