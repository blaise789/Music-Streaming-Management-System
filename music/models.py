# models.py
from django.db import models

from albums.models import Album
from users.models import User

# class Artist(models.Model):
#     name = models.CharField(max_length=100)
#     def __str__(self):
#         return self.name



class Song(models.Model):
    GENRE_CHOICES = [
        ('Pop', 'Pop'),
        ('Rock', 'Rock'),
        ('Hip-hop', 'Hip-hop')]
    title = models.CharField(max_length=150)
    duration = models.DurationField()
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='songs')
    artist = models.ForeignKey(User, on_delete=models.CASCADE,related_name='songs')
    audio_file = models.FileField(upload_to='media/songs')
    song_cover = models.ImageField(upload_to='media/images', blank=True)  
    genre=models.CharField(max_length=50, choices=GENRE_CHOICES)
    release_year = models.PositiveIntegerField(null=True,blank=True)  
    created_at=models.DateTimeField(auto_now=True)

    class  Meta:
        db_table = 'songs'
    def __str__(self):
        return self.title
class Recent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)