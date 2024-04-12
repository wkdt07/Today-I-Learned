from django.db import models

# Create your models here.

from django.conf import settings
class Movie(models.Model):
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 100)
    genre = models.CharField(max_length = 100)
    score = models.FloatField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete = models.CASCADE)
    
class Comment(models.Model):
    content = models.CharField(max_length = 100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete = models.CASCADE)
    movie = models.ForeignKey(Movie,on_delete = models.CASCADE)
