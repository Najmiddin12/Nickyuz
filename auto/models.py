from django.db import models
from django.contrib.auth.models import AbstractUser

class SignUp(AbstractUser, models.Model):
    SELLER = "seller"
    BUYER = "buyer"
    WHO = (
        (SELLER, "Seller"),
        (BUYER, "Buyer"),
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    who = models.CharField(max_length=50, choices=WHO)
    phone = models.CharField(max_length=50)
    password = models.CharField(max_length=50)



class CreateAuto(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    year = models.IntegerField()
    mileage = models.CharField(max_length=50)
    price = models.IntegerField()

