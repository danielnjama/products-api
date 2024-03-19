from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class userinfo(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    phoneNumber = PhoneNumberField()
    location = models.CharField(max_length=120)
    businessName = models.CharField(max_length=60, blank=True)

    def __str__(self):
        return self.businessName
    class Meta:
        verbose_name = "User Information"
        verbose_name_plural = "User Information"

class productCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Product Category"
        verbose_name_plural = "Product Categories"



class products(models.Model):
    category = models.ForeignKey(productCategory,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    owner = models.ForeignKey(userinfo,on_delete=models.CASCADE,related_name="owner")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
    


