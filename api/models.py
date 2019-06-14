from django.contrib.auth.models import User
from django.db import models

#Products Model
class Products(models.Model):      
    name = models.CharField(max_length=20)
    price = models.FloatField(null=False, blank=False, default=None)
    rating = models.FloatField(null=True, blank=True, default='')
     

#Rating Model
class Rating(models.Model):      
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user') 
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='product') 
    rating = models.FloatField(null=False, blank=False)