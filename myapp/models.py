from django.db import models


# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=40)
    age = models.IntegerField()
    address = models.TextField()
    image = models.ImageField()
