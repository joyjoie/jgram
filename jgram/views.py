from django.shortcuts import render, redirect,get_object_or_404,HttpResponseRedirect
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm,CommentForm,ImageForm,FollowersForm
from .models import Image,Followers,Profile, Comments
from django.contrib import messages




@login_required(login_url='/accounts/login/')
def index(request):
    images = Image.display_images()
    comments=Comments.display_comments()
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            image_id=int(request.POST.get('image_id'))
            image=Image.objects.get(id=image_id)
            comment=form.save(commit=False)
            comment.img=image
            comment.user=request.user
            comment.save()
            return redirect('index')
    else:
        form=CommentForm()

    context ={"images":images, "comments":comments , "form":form}
        
    return render(request, 'photos/index.html',context )
    


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
def profile(request, id):
    profile=Profile.objects.get(id=id)


    if request.method =='POST' and 'follower' in request.POST:
        print("Follow clicked")
        f_form=FollowersForm(request.POST)
        if f_form.is_valid():
            print("form valid")
            followz= f_form.save(commit=False)
            followz.name = str(request.user.id)+"-" + str(profile.user.id)
            print(followz.name)
            followz.save()
            messages.success(request, f'Follower added!')
            return redirect('profile',profile.id)
        else:
            print("form invalid")
    else:
        f_form=FollowersForm()
        print("Else")

    
    if request.method =='POST':
        p_form=ProfileUpdateForm(request.POST, request.FILES,instance=request.user.profile)
  
        if p_form.is_valid():
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile',profile.id)
  
    else:
        p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)


    fo=Profile.pro()

    profile=Profile.objects.get(id=id)
    current_profile=Profile.objects.get(user=request.user)



    


    return render(request, 'profile/profile.html',{"fo":fo,'p_form':p_form,'f_form':f_form,"profile":profile, "current_profile":current_profile} )


def upload(request):
    if request.method =='POST':
        form=ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form =ImageForm()
    return render(request, 'photos/addimg.html', {"form":form})

def search(request):
    if 'search' in request.GET and request.GET['search']:
        search_term = request.GET.get('search')
        profiles = Profile.search_profile(search_term)
        message = f'{search_term}'

        return render(request, 'photos/search.html',{'message':message, 'profiles':profiles})
    else:
        message = 'Enter term to search'
        return render(request, 'photos/search.html', {'message':message})



