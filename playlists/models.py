from django.utils import timezone
from django.db import models

from music.models import Song
from users.models import User

# Create your models here.
class Playlist(models.Model):
    name=models.CharField(max_length=200)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='playlists')
    songs=models.ManyToManyField(Song,related_name='playlists')
    created_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.name} by {self.user.username}"
    