from django.db import models

from shop.models.category import Category

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, default='', blank=True, null=True)
    image = models.ImageField(upload_to = 'upload/products')