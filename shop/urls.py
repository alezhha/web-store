from django.urls import path
from .views.homepage import homepage
from .views.detail import detail
from .views.cart import cart

urlpatterns = [
    path("", homepage, name = 'homepage'),
    path('detail/<int:pk>', detail, name="detail"),
    path("cart/", cart, name="cart")
]