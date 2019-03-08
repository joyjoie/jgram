from django.shortcuts import render, redirect
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Image,Followers,Profile


@login_required(login_url='/accounts/login/')

def index(request):
    images = Image.display_images() 
    return render(request, 'photos/index.html',{"images":images} )


def image(request, image):
    
    try:
        foto = Image.objects.get(id = image_id)

    except DoesNotExist:
        raise Http404()
    return render(request,"photos/image.html", {"foto":foto})