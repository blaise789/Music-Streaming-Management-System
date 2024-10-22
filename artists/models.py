from django.db import models

from users.models import User

# Create your models here.
class Artist(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="artist_profile")
    biography=models.TextField()