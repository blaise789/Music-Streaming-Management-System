from django.db import models
class User(models.Model,):
    username=models.CharField(max_length=100)
    email=models.EmailField(max_length=200,unique=True)
    password_hash = models.CharField(max_length=350)
    created_at = models.DateTimeField(auto_now=True)
    is_artist = models.BooleanField(default=False) 
     
    def __str__(self):
        return self.username
    class  Meta:
        db_table = 'users'
       
class Profile(models.Model):
      user=models.OneToOneField(User,on_delete=models.CASCADE)  
      bio=models.TextField(blank=True)
      profile_picture=models.ImageField("profile_pics",blank=True,null=True) 
      def __str__(self):
           return f"{self.user.username}'s Profile"; 
      class  Meta:
        db_table = 'profiles'