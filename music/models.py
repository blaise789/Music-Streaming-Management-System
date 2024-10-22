# models.py
from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)
    class  Meta:
        db_table = 'genres'
    def __str__(self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='albums')
    release_date = models.DateField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='albums')
    class  Meta:
        db_table = 'albums'

    def __str__(self):
        return self.title

class Song(models.Model):
    title = models.CharField(max_length=150)
    duration = models.DurationField()
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='songs')
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    audio_file = models.FileField(upload_to='songs/')
    class  Meta:
        db_table = 'songs'
    def __str__(self):
        return self.title
