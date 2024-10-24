from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from .forms import AlbumForm

from .models import Album


def album_list(request):
    albums = Album.objects.all()
    return render(request, 'album_list.html', {'albums': albums})
@login_required
def album_detail(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    return render(request, 'album_detail.html', {'album': album})
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

def is_artist(user):
   return user.is_artist;
