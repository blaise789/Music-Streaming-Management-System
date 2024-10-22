from django.db import models

class User(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField(max_length=200,unique=True)
    password_hash = models.CharField(max_length=350)
    created_at = models.DateTimeField()
    is_artist = models.BooleanField(default=False) 
     
    def __str__(self):
        return self.username
