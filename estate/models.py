from django.db import models


class Property(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500,default="#")
    img = models.ImageField(upload_to ='media/',default="#")
    price = models.CharField(max_length=40,default="#")
    # category = models.CharField(max_length=100, default='#')
    desc = models.TextField(default="#")
    slug = models.SlugField(max_length=130,default="")

    
    
    def __str__(self):
        return self.name

class Service(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    img = models.ImageField(upload_to ='media/')

    def __str__(self):
        return self.name     
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return  self.name             

class Testmonial(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to ='media/')
    desc = models.TextField(default="#")

    def __str__(self):
        return self.name        