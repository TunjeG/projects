from django.db import models
from django.forms import CharField, ImageField

# Create your models here.

class Facilities(models.Model):
    
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    comment = models.TextField()
    offer = models.BooleanField(default=False)
