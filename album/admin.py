from django.contrib import admin

from .models import Album
# Register your models here.
class AlbumAdmin(admin.ModelAdmin):

    list_display = [
        'description',
        'thumbnail',
        'created_at'
    ]

admin.site.register(Album, AlbumAdmin)