from django.contrib.auth.models import User
from django.db import models

class Music(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    release_date = models.DateField()
    # owner=models.ForeignKey(User,on_delete=models.CASCADE,related_name="music")

    def __str__(self):
        return self.title