from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('add/<int:product_id>', views.add_cart, name='add_cart'),
    path('delete/<int:product_id>', views.delete_cart_item, name='delete_cart'),
    path('remove/<int:product_id>',
         views.remove_cart_item, name='remove_cart_item'),
    path('', views.cart_details, name='cart_details'),
]
