from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Ingredient(models.Model):
    barcode = models.BigIntegerField(null=True)
    product_name = models.CharField(max_length=200,null=True)
    region = models.CharField(max_length=100, null=True)
    one_supply = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    unit = models.CharField(max_length=5, null=True)
    total_content = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    kcal = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    protein = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    fat = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    carbohydrate = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    sodium = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    cholesterol = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    foodtype = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.product_name