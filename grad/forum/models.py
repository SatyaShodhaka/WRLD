from django.db import models
from datetime import datetime 
from accounts.models import UserProfile
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    title = models.CharField(max_length=100,blank = False)
    category = models.CharField(max_length=100,blank = False,choices=[('News','News'),('Tech','Tech'),('Health','Health'),('Music','Music'),('Food','Food',),('Games','Games'),\
        ('Entertainment','Entertainment'),('Environment','Environment')])
    date = models.DateTimeField(default = datetime.now(),blank = False)
    description =  models.CharField(max_length=2000)
    article = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='forum/',default='forum/user.png',blank = True)
    report = models.IntegerField(max_length=3,default=1)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'id': self.id})

    