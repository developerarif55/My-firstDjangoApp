from django.urls import include, path
from . import views

app_name = 'album'

urlpatterns = [
    path('', views.album, name='album')

    # write code for viws details but not worked 
    # path("<int:pk>", views.blog_detail, name="blog_detail"),
]