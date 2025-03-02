# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

def home(request):
    products = Product.objects.all()  # Получаем все товары из базы
    return render(request, 'home.html', {'products': products})  # Передаём их в шаблон

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)  # Получаем товар или выдаём 404
    return render(request, 'products/product_detail.html', {'product': product})  # Передаём товар в шаблон
