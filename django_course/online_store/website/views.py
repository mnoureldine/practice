from django.shortcuts import render
from products.models import Product

from django.http import HttpResponse
from django.template import Template, Context, loader
# Create your views here.


def welcome(request):
    products_list = Product.objects.all()
    template = loader.get_template('website/welcome.html')
    context = {'products': products_list}  # update this line
    output = template.render(context)
    return HttpResponse(output)
    #return render(request, "website/welcome.html",
                  #{"products", Product.objects.all()})


