from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Product, Category


def index(request):
    """first index page"""
    return HttpResponse('First Page.Works')


def all_products_catelog(request, c_slug=None):
    """get products by slug. If not display all available products"""
    c_page = None
    products = None
    if c_slug is not None:
        c_page = get_object_or_404(Category, slug=c_slug)
        products = Product.objects.filter(category=c_page, available=True)
    else:
        products = Product.objects.filter(available=True)
    return render(request, 'category.html', {'category': c_page,
                                             'products': products})


def product_category_detail(request, c_slug, product_slug):
    """view product details"""
    try:
        product = Product.objects.get(category__slug=c_slug, slug=product_slug)
        print(product)

    except Exception as e:
        raise e
    return render(request, 'product.html', {'product': product})
