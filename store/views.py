from django.shortcuts import render
from .models import (Customer, Product,
                     Order, OrderItem,
                     ShippingAddress)

# Create your views here.

def store(request):
    products = Product.objects.all()
    context ={'products': products}
    return render(request,'store/store.html',context)

def cart(request):
    context ={}
    return render(request,'store/cart.html',context)

def check_out(request):
    context ={}
    return render(request,'store/check_out.html',context)
