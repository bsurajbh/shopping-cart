from django.db.models import Sum
from .models import Cart, CartItem
from .views import _cart_id


def cart_item_counter(request):
    """count the items in the cart"""
    count = {}
    if 'admin' in request.path:
        pass
    else:
        try:
            cart = Cart.objects.get(cart_id=_cart_id(request))
        except Cart.DoesNotExist:
            pass
        if cart:
            count = CartItem.objects.filter(cart=cart).aggregate(
                Sum('quantity'))['quantity__sum']
    return dict(cart_item_count=count if count is not None else 0)
