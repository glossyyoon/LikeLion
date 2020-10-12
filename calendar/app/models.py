from django.db import models
from django.db.models import Model
from datetime import date

# Create your models here.
class Plan(models.Model):
    objects = models.Manager()
    planName = models.CharField(max_length = 100)
    start = models.DateField(("Date"), default=date.today)
    end = models.DateField(("Date"), default=date.today)
    typeName = models.CharField(max_length = 50)


    # def __str__(self):
    #     return self.planName