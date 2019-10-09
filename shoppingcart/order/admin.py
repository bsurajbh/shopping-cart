from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from order.models import AddressBook, Order, User
from cart.models import Cart, CartItem
from shop.models import Category, Product
from django.utils.translation import gettext as _


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name', 'is_active']
    fieldsets = (
        (None, {
            'fields': ('email', 'password')
        }),
        (_('Personal Info'), {'fields': ('name',)}),
        (
            _('Permissions'),
            {'fields': ('is_active', 'is_staff', 'is_superuser')}
        ),
        (
            _('Important Dates'),
            {'fields': ('last_login',)}
        )
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email',)
        }),
    )


admin.site.register(User, UserAdmin)
admin.site.register(AddressBook)
admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(CartItem)


class CategoryAdmin(admin.ModelAdmin):
    """category admin field"""
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    """product admin fields"""
    list_display = ['name', 'price', 'stock',
                    'available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)
