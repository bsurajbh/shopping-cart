from django.db import models
from shop.models import Product


class Cart(models.Model):
    """user cart"""
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'Cart'
        ordering = ('date_added',)

    def __str__(self):
        return self.cart_id


class CartItem(models.Model):
    """storing cart items"""
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    quantity = models.IntegerField()

    class Meta:
        db_table = 'CartItem'

    def product_total(self):
        """calculating total product price"""
        return self.product.price * self.quantity
