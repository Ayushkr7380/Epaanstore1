from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class flavourpaan(models.Model):
    name = models.CharField(max_length=300)
    price = models.FloatField(null=False)
    description = models.CharField(max_length=400)
    image = models.ImageField(null=True)
    offers = models.CharField(max_length=400,null=True,default='')
    benefit = models.CharField(max_length = 1000,default='')
    date = models.DateField(auto_now_add=True)

class sweetpaan(models.Model):
    name = models.CharField(max_length=300)
    price = models.FloatField(null=False)
    description = models.CharField(max_length=400)
    image = models.ImageField(null=True)
    offers = models.CharField(max_length=400,null=True,default='')
    benefit = models.CharField(max_length = 1000,default='')
    date = models.DateField(auto_now_add=True)

class paanaroma(models.Model):
    name = models.CharField(max_length=300)
    price = models.FloatField(null=False)
    description = models.CharField(max_length=400)
    image = models.ImageField(null=True)
    offers = models.CharField(max_length=400,null=True,default='')
    benefit = models.CharField(max_length = 1000,default='')
    date = models.DateField(auto_now_add=True)

class specialpaan(models.Model):
    name = models.CharField(max_length=300)
    price = models.FloatField(null=False)
    description = models.CharField(max_length=400)
    image = models.ImageField(null=True)
    offers = models.CharField(max_length=400,null=True,default='')
    benefit = models.CharField(max_length = 1000,default='')
    date = models.DateField(auto_now_add=True)

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    price = models.FloatField(null=False,default=0)
    image = models.ImageField(null=True,default='')
    quantity = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True)

class Address(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=1000)
    address2 = models.CharField(max_length=1000,default='')
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    zip = models.CharField(max_length=10)

class Myorder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='order_addresses')
    p_id = models.IntegerField(default=0)
    p_name = models.CharField(max_length=300)
    p_price = models.CharField(max_length=4)
    p_image = models.ImageField(default='')
    p_quantity = models.CharField(max_length=4) 
    o_date = models.DateTimeField(auto_now_add=True)
    p_deliverytime = models.CharField(max_length=100,default="")
    status = models.CharField(max_length=200,default='Order Confirmed')

class Contact(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=1000)
    query = models.CharField(max_length=5000)

    
    

