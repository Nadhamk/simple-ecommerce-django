from django.db import models

# Create your models here.
class Data(models.Model):
    name=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    image=models.FileField()
    address=models.CharField(max_length=20)
    phone=models.CharField(max_length=20)
    
    def __str__(self):
        return self.name

class Login(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    type=models.IntegerField()
    
    def __str__(self):
        return self.username

class Product(models.Model):
    productname=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    price=models.CharField(max_length=255)
    photo=models.FileField()
    
    def __str__(self):
        return self.productname
    
class Buy(models.Model):
    username=models.ForeignKey(Data,on_delete=models.CASCADE)
    productname=models.ForeignKey(Product,on_delete=models.CASCADE)
    date=models.CharField(max_length=20)
    



    


    

