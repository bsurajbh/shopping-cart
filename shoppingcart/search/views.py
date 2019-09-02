from django.shortcuts import render
from django.db.models import Q
from shop.models import Product


def Search(request):
    """search site functionality"""
    products = None
    query = None
    print(request.GET)
    if 'q' in request.GET:
        query = request.GET.get('q')
        products = Product.objects.all().filter(
            Q(name__contains=query) | Q(description__contains=query))
    return render(request, 'search.html', {'query': query, 'products': products})
