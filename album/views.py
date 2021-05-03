from django.shortcuts import render
from .models import *


# Create your views here.
def album(request):

    album = Album.objects.all()

    context ={
        'album':album

    }


    return render(request, 'album/index.html', context)
    
# write code for views detail but not worked
# def album(request, pk):
#     album = Album.objects.get(pk=pk)
   
#     context = {"album": album}
#     return render(request, "album/blog_detail.html", context)