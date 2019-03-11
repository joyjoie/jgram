from django.shortcuts import render, redirect
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm
from .models import Image,Followers,Profile
from django.contrib import messages

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