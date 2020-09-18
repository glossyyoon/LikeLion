from django.db import models

# Create your models here.
class melonList(models.Model):
    songName = models.CharField(max_length=100)
    singerName = models.CharField(max_length=100)
    rank = models.IntegerField(default=0)
    imgSrc = models.TextField(blank=True)