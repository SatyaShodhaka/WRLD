from django.db import models
from datetime import datetime 
from accounts.models import UserProfile
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100,blank = False)
    category = models.CharField(max_length=100,blank = False,choices=[('News','News'),('Tech','Tech'),('Health','Health'),('Music','Music'),('Food','Food',),('Games','Games'),\
        ('Entertainment','Entertainment'),('Environment','Environment')])
    date = models.DateTimeField(default = datetime.now(),blank = False)
    description =  models.CharField(max_length=1000)
    image = models.ImageField(upload_to='forum',blank = False)
    
    def __str__(self):
        return self.title

    