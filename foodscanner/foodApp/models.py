from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length = 100)
    carbonhydrate = models.IntegerField()
    fat = models.IntegerField()
    sodium = models.IntegerField()
    protein = models.IntegerField()
    calorie = models.IntegerField()
    cholesterol = models.IntegerField()