from django.db import models

# Create your models here.
class Youtube(models.Model):
    channel = models.CharField(max_length = 50)
    creator = models.CharField(max_length = 50)
    prefer = models.IntegerField()
    live = models.BooleanField()
    subscribe = models.IntegerField()
    link1 = models.TextField(blank = True)
    link2 = models.TextField(blank = True)
    link3 = models.TextField(blank = True)
    text = models.TextField(max_length = 2000, blank=True)
    summaty = models.TextField(max_length=200, blank=True)
    photo = models.ImageField(upload_to = "image", blank=True)
    objects = models.Manager()
