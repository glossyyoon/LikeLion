from django.db import models
from django import forms

class UploadFileForm(forms.Form):
    titles = forms.CharField(max_length=50)
    file = forms.FileField()

# Create your models here.
class picEdit(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length = 100)
    explain = models.TextField()
    pic = models.ImageField(blank=True)
    day = models.DateTimeField(auto_now=True)

