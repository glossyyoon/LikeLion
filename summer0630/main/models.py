from django.db import models

# Create your models here.
class Members(models.Model):
    memberId = models.IntegerField(primary_key=True)
    memberName = models.CharField(max_length = 123)
    home = models.CharField(max_length = 123)

class Orders(models.Model):
    objects = models.Manager()
    memberId = models.ForeignKey(Members, on_delete=models.SET_NULL, null=True, blank = True)
    orderId = models.IntegerField(primary_key=True)

class Goods(models.Model):
    objects = models.Manager()
    productName = models.CharField(max_length = 50)
    productId = models.IntegerField(primary_key=True)
    price = models.IntegerField(max_length = 30)

class Sheets(models.Model):
    objects = models.Manager()
    contents1 = models.ForeignKey(Members, on_delete=models.SET_NULL, null=True, blank = True)
    contents2 = models.ForeignKey(Orders, on_delete=models.SET_NULL, null=True, blank = True)
    contents3 = models.ForeignKey(Goods, on_delete=models.SET_NULL, null=True, blank = True)
    number = models.IntegerField(primary_key=True)
