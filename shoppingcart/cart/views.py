from django.shortcuts import render


def _cart_id(request):
    """check serssion exists"""
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart
