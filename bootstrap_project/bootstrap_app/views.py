from django.shortcuts import render
from . models import Product

def product_list(request):
    if not Product.objects.exists():
        Product.objects.create(name='Ultrabook Laptop', description='Lightweight and powerful laptop', price='1500')
        Product.objects.create(name='Flagship Smartphone', description='Premium 5G smartphone with advanced camera', price='1200')
        Product.objects.create(name='Bluetooth Earbuds', description='True wireless earbuds with deep bass', price='180')
        Product.objects.create(name='Fitness Tracker', description='Monitor your health and activity levels', price='150')
        Product.objects.create(name='E-Reader', description='Read e-books with an eye-friendly display', price='300')

    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

