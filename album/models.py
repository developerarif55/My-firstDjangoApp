from django.db import models


# Create your models here.

class Album(models.Model):

    thumbnail = models.ImageField(upload_to='album5/photo')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
