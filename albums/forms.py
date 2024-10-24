from django import forms
from .models import Album


class AlbumForm(forms.ModelForm):
    class Meta:
        
        exclude=['artist']
        model = Album
        fields = ['title', 'artist']