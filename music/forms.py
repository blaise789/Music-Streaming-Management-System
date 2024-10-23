# forms.py
from django import forms
from .models import Song
# , Album

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title',  'artist', 'audio_file','song_cover','genre']

# class AlbumForm(forms.ModelForm):
#     class Meta:
        
#         exclude=['artist']
#         model = Album
#         fields = ['title', 'artist', 'genre']
