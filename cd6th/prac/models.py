from django.db import models

# Create your models here.
class prac(models.Model):
    objects = models.Manager()
    channel = models.CharField(max_length = 50, default="")
    new = models.FileField(max_length=3000, default="")
    photo = models.ImageField(upload_to = "image", blank=True)
    