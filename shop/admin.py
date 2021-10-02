from django.contrib import admin
from .models.category import Category
from .models.customer import Customer
from .models.order import Order
from .models.product import Product

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'email', 'password']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", ]

class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'quantity', 'phone', 'address', 'date', 'status', 'price']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price', 'category', 'description', 'image']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Product, ProductAdmin)
