from django.db import models


# Create your models here.
class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    age = models.IntegerField()
    address = models.TextField()
    image = models.ImageField()
    
