# models.py
from django.db import models

from users.models import User

# class Artist(models.Model):
#     name = models.CharField(max_length=100)
#     def __str__(self):
#         return self.name

# class Album(models.Model):
#     # genre choices
#     GENRE_CHOICES = [
#         ('Pop', 'Pop'),
#         ('Rock', 'Rock'),
#         ('Hip-hop', 'Hip-hop'),
#         ('R&B', 'R&B')]
    
#     title = models.CharField(max_length=200)
#     artist= models.ForeignKey(User, on_delete=models.CASCADE, related_name='albums')
#     genre=models.CharField(max_length=50,name="genre" ,choices=GENRE_CHOICES)
#     release_date = models.DateField(auto_now=True)
#     class  Meta:
#         db_table = 'albums'

#     def __str__(self):
        # return self.title

class Song(models.Model):
    GENRE_CHOICES = [
        ('Pop', 'Pop'),
        ('Rock', 'Rock'),
        ('Hip-hop', 'Hip-hop')]
    title = models.CharField(max_length=150)
    duration = models.DurationField()
    # album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='songs')
    artist = models.ForeignKey(User, on_delete=models.CASCADE)
    audio_file = models.FileField(upload_to='media/')
    genre=models.CharField(max_length=50, choices=GENRE_CHOICES)
    class  Meta:
        db_table = 'songs'
    def __str__(self):
        return self.title
