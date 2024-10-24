from django.db import models

from users.models import User

# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=200)
    artist= models.ForeignKey(User, on_delete=models.CASCADE, related_name='albums')
    release_date = models.DateField(auto_now=True)
    class  Meta:
        db_table = 'albums'

    def __str__(self):
        return self.title