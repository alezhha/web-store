from django.contrib import admin
from .models.category import Category
from .models.customer import Customer
from .models.order import Order
from .models.product import Product
from django.utils.safestring import mark_safe

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'email', 'password']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", ]

class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'quantity', 'phone', 'address', 'date', 'status', 'price']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price', 'category', 'description', 'image', 'show_image']

    def show_image(self, img_obj):
        if img_obj.image:
            return mark_safe('<img src={} width=70px/>'.format(img_obj.image.url))
        return None

    show_image.__name__ = "Image"

admin.site.register(Category, CategoryAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Product, ProductAdmin)
