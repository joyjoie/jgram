from django.db import models
import datetime as dt
# Create your models here.

class Image(models.Model):
    name = models.CharField(max_length=60)
    image = models.ImageField(upload_to="image/")
    comments= models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

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

class Followers(models.Model):
    name = models.CharField(max_length=60)

    def save_followers(self):
        self.save()


class Profile(models.Model):
    user = models.CharField(max_length=60)
    bio =models.TextField()
    image=models.ForeignKey(Image)
    followers=models.ForeignKey(Followers)
    
    
    
    def save_profile(self):
        self.save()

