from django.contrib import admin

# Register your models here.
from .models import Image,Profile,Followers,Comments

class ImageAdmin(admin.ModelAdmin):
    filter_horizontal =('Profile',)


admin.site.register(Image)
admin.site.register(Profile)
admin.site.register(Comments)
admin.site.register(Followers)