from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    description = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=50,default='')
    website = models.URLField(default='')
    image = models.ImageField(upload_to='accounts/',default='accounts/user.png',blank = True)

    def __str__(request):
        return user.username
        
#creating the userprofile for the superusers
def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])
        

post_save.connect(create_profile,sender=User)