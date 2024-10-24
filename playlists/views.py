from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib import messages
from .models import Playlist
from .forms import PlaylistForm  # You will create this form in the next step

class PlaylistListView(View):
    def get(self, request):
        playlists = Playlist.objects.filter(user=request.user)
        return render(request, 'playlists_list.html', {'playlists': playlists})

class PlaylistDetailView(View):
    def get(self, request, pk):
        playlist = get_object_or_404(Playlist, pk=pk)
    
        return render(request, 'playlist_detail.html', {'playlist': playlist})

class PlaylistCreateView(View):
    def get(self, request):
        form = PlaylistForm()
        return render(request, 'playlist_form.html', {'form': form})

    def post(self, request):
        form = PlaylistForm(request.POST)
        if form.is_valid():
            playlist = form.save(commit=False)
            playlist.user = request.user
            playlist.save()
            messages.success(request, 'Playlist created successfully!')
            return redirect('playlist_list')
        return render(request, 'playlist_form.html', {'form': form})

class PlaylistEditView(View):
    def get(self, request, pk):
        playlist = get_object_or_404(Playlist, pk=pk)
        form = PlaylistForm(instance=playlist)
        return render(request, 'playlist_form.html', {'form': form, 'playlist': playlist})

    def post(self, request, pk):
        playlist = get_object_or_404(Playlist, pk=pk)
        form = PlaylistForm(request.POST, instance=playlist)
        if form.is_valid():
            form.save()
            messages.success(request, 'Playlist updated successfully!')
            return redirect('playlist_detail', pk=playlist.pk)
        return render(request, 'playlist_form.html', {'form': form, 'playlist': playlist})

class PlaylistDeleteView(View):
    def get(self, request, pk):
        playlist = get_object_or_404(Playlist, pk=pk)
        return render(request, 'playlist_confirm_delete.html', {'playlist': playlist})

    def post(self, request, pk):
        playlist = get_object_or_404(Playlist, pk=pk)
        playlist.delete()
        messages.success(request, 'Playlist deleted successfully!')
        return redirect('playlist_list')
