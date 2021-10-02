from django.shortcuts import render
from ..models import product
from ..models import category
from ..models import order
from ..models import customer



def homepage(request):
    products = product.Product.objects.all()
    categories = category.Category.objects.all()
    customers = customer.Customer.objects.all()
    orders = order.Order.objects.all()
    return render(request, 'index.html', {"orders":orders,"categories":categories, "products":products, "customers":customers})