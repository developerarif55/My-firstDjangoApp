
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
   
    path('', include('blog.urls', namespace='blog')),
    # path('myapp/', include('myapp.urls', namespace='myapp')),
    # path('album/', include('album.urls', namespace='album')),
    path('summernote/', include('django_summernote.urls'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)
