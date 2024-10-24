from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from music.models import Song

from .forms import AlbumForm

from .models import Album


def album_list(request):
    albums = Album.objects.all()
    return render(request, 'album_list.html', {'albums': albums})
@login_required
def album_detail(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    return render(request, 'album_details.html', {'album': album})
@login_required
def album_create(request):
    print(request.user)
    
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            album=form.save(commit=False)
            album.artist=request.user
            album.save()
            return redirect('album_list')
    else:
        form = AlbumForm()
    return render(request, 'album_form.html', {'form': form})
@login_required
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

@login_required
def add_song_to_album(request, album_id):
    album = get_object_or_404(Album, id=album_id)  # Fetch the album

    if request.method == 'POST':
        song_id = request.POST.get('song')  # Get the selected song ID
        song = get_object_or_404(Song, id=song_id)  # Fetch the song
        
        # Add the song to the album
        album.songs.add(song)  # Add the song to the album's ManyToMany field
        messages.success(request, f'Song "{song.title}" has been added to the album "{album.title}".')
        return redirect('album_details', album_id=album.id)  # Redirect to the album details page

    return redirect('album_list')  # Fallback if the request method is not POST
