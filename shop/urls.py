from django.urls import path
from .views.homepage import homepage
from .views.detail import detail
from .views.cart import cart, cartRem, cartAdd
from .views.register import register
from .views.signin import signin
from .views.signout import signout
from .views.getByCat import get_by_category
from .views.search import search
from .views.order import order

urlpatterns = [
    path("", homepage, name = 'homepage'),
    path('detail/<int:pk>', detail, name="detail"),
    path("cart", cart, name="cart"),
    path("getByCat/<int:pk>", get_by_category, name="getByCat"),
    path("register", register, name='register'),
    path("signin", signin, name='signin'),
    path("signout", signout, name='signout'),
    path("cartAdd/<int:pk>", cartAdd, name='cartAdd'),
    path("cartAdd/cartRem/<int:pk>", cartRem, name='cartRem'),
    path("cartRem/<int:pk>", cartRem, name='cartRem'),
    path("search", search, name='search'),
    path("order", order, name="order")
]