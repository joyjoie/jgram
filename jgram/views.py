from django.shortcuts import render, redirect,get_object_or_404,HttpResponseRedirect
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm
from .models import Image,Followers,Profile
from django.contrib import messages

@login_required(login_url='/accounts/login/')



@login_required(login_url='/accounts/login/')
def index(request):
    images = Image.display_images()
     
      
    return render(request, 'photos/index.html',{"images":images} )
    

def image(request, id,slug):
    image=get_object_or_404()
    try:
        foto = Image.objects.get(id = image_id, slug=slug)

    except DoesNotExist:
        raise Http404()

    is_liked = False
    if image.likes.filter(id = request.user.id).exists():
        is_liked = True

    return render(request,"photos/image.html", {"foto":foto,"is_liked":is_liked, "total_likes":image.total_likes(), "image":image})

def like_post(request):
    image= get_object_or_404(Image, id=request.POST.get('image_id'))
    image.likes.add(request.user)
    if image.likes.filter(id=request.user.id).exists():
        image.likes.remove(request.user)
        is_liked=False
    else:
        image.likes.add(request.user)
        is_liked =True
    return HttpResponseRedirect(image.get_absolute_url()) 

@login_required
def profile(request):
    if request.method =='POST':
        p_form=ProfileUpdateForm(request.POST, request.FILES,instance=request.user.profile)
  
        if p_form.is_valid():
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
  
    else:
        p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)


    fo=Profile.pro()
    return render(request, 'profile/profile.html',{"fo":fo,'p_form':p_form} )

def upload(request):
    return render(request, upload.html)
