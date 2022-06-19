from django.shortcuts import render
from .models import Product

# Create your views here.
def detail(request, id):
    product = Product.objects.get(pk=id)
    return render(request, "website/product.html", {"product": product})

def products(request):
    return render(request, "website/products.html")
