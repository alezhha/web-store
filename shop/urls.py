from django.urls import path
from .views.homepage import homepage

urlpatterns = [
    path("", homepage, name = 'homepage')
]