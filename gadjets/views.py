from django.shortcuts import render
from .models import Product, Tag
from django.core.paginator import Paginator

def product_list(request):
    tag_name = request.GET.get('tag')
    if tag_name:
        products = Product.objects.filter(tags__name=tag_name)
    else:
        products = Product.objects.all()
    tags = Tag.objects.all()
    return render(request, 'gadjets/product_list.html', {'products': products, 'tags': tags})

