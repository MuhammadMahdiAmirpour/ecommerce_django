from django.shortcuts import render
from .models import Product

# Create your views here.

def index(request):
    product_objects = Product.objects.all()
    item_name = request.GET.get('item_name')
    if all([item_name!='', item_name is not None]):
        product_objects = product_objects.filter(title__icontains = item_name)
    return render(request, 'shop/index.html', {'product_objects': product_objects})

