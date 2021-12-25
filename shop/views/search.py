from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from ..models.product import Product

def search(request):
    if request.method == "POST":
        searched_product_from_input = request.POST.get("searched_product")
        print(searched_product_from_input)
        searched_products = Product.objects.filter(name__contains=searched_product_from_input)
        return render(request, "search.html", {"searched_product_from_input":searched_product_from_input, "searched_products":searched_products })
