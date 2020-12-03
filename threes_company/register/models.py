from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class User_Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    phone = models.CharField(max_length=10)
    age = models.IntegerField()
    address = models.CharField(max_length=1024)
    bio = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.user.username} User_Profile'
    