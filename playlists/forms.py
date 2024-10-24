from django import forms
from .models import Playlist

class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ['name']
        widgets = {'name': forms.TextInput(attrs={
             'class'
             : 
             'form-control'
             , 
             'placeholder'
             : 
             'Enter playlist name'
             }),
        }