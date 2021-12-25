from django.db import models
from .category import Category
from .product import Product
from .customer import Customer
import datetime


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=datetime.datetime.today())
    status = models.BooleanField(default = False)
    price = models.IntegerField(default=0)


    def placeOrder(self):
        self.save()

    def get_order_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by("-date")

