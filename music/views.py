# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Song, Album
from .forms import SongForm, AlbumForm
from mutagen import File  # Import the mutagen library

def song_create(request):
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the song object without saving to the database yet
            song = form.save(commit=False)

            # Get the uploaded audio file
            audio_file = request.FILES['audio_file']

            # Use mutagen to get the audio file duration
            audio = File(audio_file)
            duration = audio.info.length  # Duration in seconds

            # Convert the duration to a timedelta and set it to the song object
            song.duration = duration  # Assuming you have a DurationField in your Song model

            # Now save the song to the database
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
    return render(request, 'song_detail.html', {'song': song})



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

def song_delete(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    if request.method == 'POST':
        song.delete()
        return redirect('song_list')
    return render(request, 'song_confirm_delete.html', {'song': song})

# Album Views
def album_list(request):
    albums = Album.objects.all()
    return render(request, 'album_list.html', {'albums': albums})

def album_detail(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    return render(request, 'album_detail.html', {'album': album})

def album_create(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('album_list')
    else:
        form = AlbumForm()
    return render(request, 'album_form.html', {'form': form})

def album_update(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('album_list')
    else:
        form = AlbumForm(instance=album)
    return render(request, 'album_form.html', {'form': form})

def album_delete(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    if request.method == 'POST':
        album.delete()
        return redirect('album_list')
    return render(request, 'album_confirm_delete.html', {'album': album})
