from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse
# Create your models here.

class Image(models.Model):
    name = models.CharField(max_length=60)
    image = models.ImageField(upload_to="image/")
    caption= models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    likes =models.ManyToManyField( User, related_name='likes', blank=True)
    def save_image(self):
        self.save()


    @classmethod
    def display_images(cls):
        return cls.objects.all()


    @classmethod
    def index(cls):
        today = dt.date.today()
        yo = cls.objects.filter(pub_date__date=today)
        return yo

    def get_absolute_url(self): 
        return reverse('index')

    def total_likes(self):
        return self.likes.count()
class Followers(models.Model):
    name = models.CharField(max_length=60)

    def save_followers(self):
        self.save()

    @classmethod
    def foll(cls):
        return cls.objects.all()


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.CharField(max_length=60)
    image=models.ImageField(default='default.jpg',upload_to='profile_pics')
    followers=models.ForeignKey(Followers)
    
    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save_profile(self):
       self.save() 
       
    @classmethod
    def pro(cls):
        return cls.objects.all()
    def get_absolute_url(self): 
        return reverse('index')

class Comments(models.Model):
    img=models.ForeignKey(Image)
    user=models.ForeignKey( User)
    comment= models.CharField(max_length=60)

    def save_comments(self):
        self.save()

