from django.conf.urls import url ,include

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
   
    url(r'^$',views.index,name='index'),
    url(r'^image/(\d+)',views.image,name ='image'),
    url(r'^profile/(\d+)?$', views.profile, name='profile'),
    url(r'^like/$', views.like_post, name='like_post'),
    url(r'^search/', views.search, name='search'),
    url(r'^upload/$', views.upload, name='upload'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)