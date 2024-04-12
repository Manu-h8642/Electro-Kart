from django.db import models

# Create your models here.
class cdb(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    des = models.CharField(max_length=200,null=True,blank=True)
    image = models.ImageField(upload_to="images",null=True,blank=True)

class pdb(models.Model):
    cname = models.CharField(max_length=100,null=True,blank=True)
    pname = models.CharField(max_length=100,null=True,blank=True)
    desc = models.CharField(max_length=200,null=True,blank=True)
    price = models.IntegerField(null=True,blank=True)
    image1 = models.ImageField(upload_to="images",null=True,blank=True)
    image2 = models.ImageField(upload_to="images",null=True,blank=True)
    image3 = models.ImageField(upload_to="images",null=True,blank=True)

