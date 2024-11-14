from datetime import timedelta
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse
from playlists.models import Playlist
from users.models import User
from .models import Recent, Song, Album  # Ensure Album is imported
from .forms import SongForm
from mutagen import File  
def index(request):
    #Display recent songs
    if request.user.is_authenticated:
        recent = list(Recent.objects.filter(user=request.user).values('song_id').order_by('-id'))
        recent_id = [each['song_id'] for each in recent][:5]
        recent_songs_unsorted = Song.objects.filter(id__in=recent_id,recent__user=request.user)
        recent_songs = list()
        for id in recent_id:
            recent_songs.append(recent_songs_unsorted.get(id=id))
    else:
        recent = None
        recent_songs = None

    first_time = False
    #Last played song
    if  request.user.is_authenticated:
        last_played_list = list(Recent.objects.filter(user=request.user).values('song_id').order_by('-id'))
        if last_played_list:
            last_played_id = last_played_list[0]['song_id']
            last_played_song = Song.objects.get(id=last_played_id)
        else:
            first_time = True
            last_played_song = None

    else:
        first_time = True
        last_played_song = None

    #Display all songs
    songs = Song.objects.all()

    #Display few songs on home page
    songs_all = list(Song.objects.all().values('id').order_by('?'))
    sliced_ids = [each['id'] for each in songs_all][:5]
    indexpage_songs = Song.objects.filter(id__in=sliced_ids)
        # Display Rock Songs
    songs_rock = list(Song.objects.filter(genre='Rock').values('id'))
    sliced_ids = [each['id'] for each in songs_rock][:5]
    indexpage_rock_songs = Song.objects.filter(id__in=sliced_ids)
    
    if len(request.GET) > 0:
        search_query = request.GET.get('q')
        filtered_songs = songs.filter(Q(title__icontains=search_query)).distinct()
        context = {'all_songs': filtered_songs,'last_played':last_played_song,'query_search':True}
        return render(request, 'index.html', context)

    context = {
        'all_songs':indexpage_songs,
        'recent_songs': recent_songs,
        'first_time': first_time,
        'query_search':False,
        'rock_songs':indexpage_rock_songs,
        'last_played':last_played_song,
    }
    print(context)
    return render(request, 'index.html', context=context)


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
    first_time = False
    #Last played song
    if request.user.is_authenticated:
        last_played_list = list(Recent.objects.filter(user=request.user).values('song_id').order_by('-id'))
        if last_played_list:
            last_played_id = last_played_list[0]['song_id']
            last_played_song = Song.objects.get(id=last_played_id)
        else:
          last_played_song=None
    else:
        first_time = True
        last_played_song=None
        
    return render(request, 'songs_list.html', {
        'first_time': first_time,  
        'songs': songs,
        'all_genres': all_genres,
        'all_artists': all_artists,
        'query': query,
        'selected_genre': genre,
        'selected_artist': artist,
        'last_played': last_played_song,
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
            return redirect('song_details',song.id)
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
@login_required(login_url='login')
def play_song(request, song_id):
    songs = Song.objects.filter(id=song_id).first()
    # Add data to recent database
    if list(Recent.objects.filter(song=songs,user=request.user).values()):
        data = Recent.objects.filter(song=songs,user=request.user)
        data.delete()
    data = Recent(song=songs,user=request.user)
    data.save()
    return redirect('song_list')
@login_required(login_url='login')
def play_song_index(request, song_id):
    songs = Song.objects.filter(id=song_id).first()
    # Add data to recent database
    if list(Recent.objects.filter(song=songs,user=request.user).values()):
        data = Recent.objects.filter(song=songs,user=request.user)
        data.delete()
    data = Recent(song=songs,user=request.user)
    data.save()
    return redirect('index')

def recent(request):
    #Last played song
    last_played_list = list(Recent.objects.values('song_id').order_by('-id'))
    if last_played_list:
        last_played_id = last_played_list[0]['song_id']
        last_played_song = Song.objects.get(id=last_played_id)
    else:
        last_played_song = Song.objects.get(id=7)
    recent = list(Recent.objects.filter(user=request.user).values('song_id').order_by('-id'))
    if recent and not request.user.is_anonymous :
        recent_id = [each['song_id'] for each in recent]
        recent_songs_unsorted = Song.objects.filter(id__in=recent_id,recent__user=request.user)
        recent_songs = list()
        for id in recent_id:
            recent_songs.append(recent_songs_unsorted.get(id=id))
    else:
        recent_songs = None
    if len(request.GET) > 0:
        search_query = request.GET.get('q')
        filtered_songs = recent_songs_unsorted.filter(Q(title__icontains=search_query)).distinct()
        context = {'recent_songs': filtered_songs,'last_played':last_played_song,'query_search':True}
        return render(request, 'recent.html', context)

    context = {'recent_songs':recent_songs,'last_played':last_played_song,'query_search':False}
    return render(request, 'recent.html', context=context)
def rock_songs(request):
    rock_songs = Song.objects.filter(genre='Rock')
    #Last played song
    last_played_list = list(Recent.objects.values('song_id').order_by('-id'))
    if last_played_list:
        last_played_id = last_played_list[0]['song_id']
        last_played_song = Song.objects.get(id=last_played_id)
    else:
        last_played_song = Song.objects.get(id=7)

    query = request.GET.get('q')

    if query:
        rock_songs = Song.objects.filter(Q(title__icontains=query)).distinct()
        context = {'rock_songs': rock_songs}
        return render(request, 'rock_songs.html', context)

    context = {'rock_songs':rock_songs,'last_played':last_played_song}
    return render(request, 'rock_songs.html',context=context)
@login_required()
def play_recent_song(request, song_id):
    songs = Song.objects.filter(id=song_id).first()
    # Add data to recent database
    if list(Recent.objects.filter(song=songs,user=request.user).values()):
        data = Recent.objects.filter(song=songs,user=request.user)
        data.delete()
    data = Recent(song=songs,user=request.user)
    data.save()
    return redirect('recent')

def mymusic(request):
    return render(request, 'mymusic.html')