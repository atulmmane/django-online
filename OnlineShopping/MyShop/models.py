from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    cname=models.CharField(max_length=30)

    def __str__(s):
        return s.cname

class Product(models.Model):
    pname=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    #pimage=models.ImageField(upload_to='images/')
    category=models.ForeignKey(Category,on_delete=models.CASCADE)



class Cart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
