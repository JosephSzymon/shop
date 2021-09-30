from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=50)
    price = models.IntegerField()
    product_type = models.ChoiceField
    image = models.ImageField

class User(models.Model):
    mail = models.EmailField
    password = models.CharField(max_length=50)
    user_name - models.CharField(max_lenght=50)