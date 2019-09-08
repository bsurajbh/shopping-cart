from django.shortcuts import render, redirect
from . models import Cart, CartItem
from shop.models import Product
from django.core.exceptions import ObjectDoesNotExist


def _cart_id(request):
    """check serssion exists"""
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def add_cart(request, product_id):
    """add item to the cart"""
    product = Product.objects.get(id=product_id)
    try:
        # get cart
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        # create cart
        cart = Cart.objects.create(
            cart_id=_cart_id(request)
        )
        cart.save()
    try:
        # add products to cart
        cart_item = CartItem.objects.get(product=product, cart=cart)
        if(cart_item.quantity < cart_item.product.stock):
            cart_item.quantity += 1
            cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product=product, quantity=1, cart=cart
        )
        cart_item.save()
    return redirect('cart:cart_details')


def cart_details(request, total=0, counter=0, cart_items=None):
    """get cart details"""
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, active=True)
        for item in cart_items:
            total += item.product.price * item.quantity
            counter += item.quantity
    except ObjectDoesNotExist:
        pass
    return render(request, 'cart.html', dict(cart_items=cart_items, total=total,
                                             counter=counter))
