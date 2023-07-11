from django.shortcuts import render
from django.http import JsonResponse
from .models import Product
from .cart import Cart

# Create your views here.
def home(request):
    product = Product.objects.get(pk=2)
    cart = Cart(request)
    data = cart.add_product(product)
    return JsonResponse(data)