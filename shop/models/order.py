from django.db import models
from .category import Category
from .customer import Customer
import datetime


class Order(models.Model):
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=datetime.datetime.today())
    status = models.BooleanField(default = False)
    price = models.IntegerField(default=1)


    def placeOrder(self):
        self.save()

    def get_order_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by("-date")

