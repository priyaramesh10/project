from django.db import models
#from django.contrib.auth.models import User




'''class User(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    email    = models.EmailField(max_length=100)
    password = models.IntegerField()
    

    def __str__(self):
        return self.username'''



class Product(models.Model):
    product_name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    price = models.IntegerField()    


    def __str__(self):
        return self.product_name