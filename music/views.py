from datetime import timedelta
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from playlists.models import Playlist
from users.models import User
from .models import Song, Album  # Ensure Album is imported
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
            song.artist = request.user 
            print(song.artist)
            song.save()
            
            messages.success(request, f'Song "{song.title}" has been created successfully.')
            return redirect('song_list')
    else:
        form = SongForm()
    return render(request, 'song_form.html', {'form': form})

def song_list(request):
    query = request.GET.get('q', '')
    genre = request.GET.get('genre', '')
    artist = request.GET.get('artist', '')

    songs = Song.objects.all()

    if query:
        songs = songs.filter(title__icontains=query)
    if genre:
        songs = songs.filter(genre__icontains=genre)
    if artist:
        songs = songs.filter(artist__username__icontains=artist)

    all_genres = Song.objects.values_list('genre', flat=True).distinct()  
    all_artists = User.objects.values_list('username', flat=True).distinct()

    return render(request, 'songs_list.html', {
        'songs': songs,
        'all_genres': all_genres,
        'all_artists': all_artists,
        'query': query,
        'selected_genre': genre,
        'selected_artist': artist,
    })
@login_required(login_url="/user/login",redirect_field_name=None)
def song_detail(request, song_id):
      song = get_object_or_404(Song, id=song_id)
      playlists = Playlist.objects.filter(user=request.user) 
      if request.method == 'POST':
          playlist_name = request.POST.get('playlist')
          playlist = Playlist.objects.get(name=playlist_name, user=request.user)
          playlist.songs.add(song)
          messages.success(request, f'Song "{song.title}" has been added to "{playlist.name}".')
      return render(request, 'song_details.html', {'song': song, 'playlists': playlists})
    
@login_required(login_url="/user/login",redirect_field_name=None)
def song_update(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES, instance=song)
        if form.is_valid():
            form.save()
            messages.success(request, f'Song "{song.title}" has been updated successfully.')
            return redirect('song_list')
    else:
        form = SongForm(instance=song)
    return render(request, 'song_form.html', {'form': form})

@login_required(login_url="/user/login",redirect_field_name=None)
def song_delete(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    if request.method == 'POST':
        song.delete()
        messages.success(request, f'Song "{song.title}" has been deleted successfully.')
        return redirect('song_list')
    return render(request, 'song_confirm_delete.html', {'song': song})
def song_play(request, song_id):
    song = get_object_or_404(Song, pk=song_id)

    # Handle the song playback logic here
    # This might involve streaming the audio file, redirecting to a streaming service,
    # or generating a download link.

    # Example: Streaming the audio file directly
    response = HttpResponse(content_type='audio/mpeg')
    response['Content-Disposition'] = f'attachment; filename="{song.title}.mp3"'
    with song.audio_file.open('rb') as f:
        response.write(f.read())
    return response