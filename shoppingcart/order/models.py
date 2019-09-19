from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser

# Class = Address()


class User(AbstractBaseUser):
    """user model from abstract base class"""
    email = models.EmailField(max_length=255, blank=False, unique=True)

    USERNAME_FIELD = ('email')


class Order(models.Model):
    """order model class"""
    token = models.CharField(max_length=255, blank=True)
    total = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Total Rupees')
    email_address = models.EmailField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # address = models.ForeignKey(Address, on_delete=models.CASCADE)


class AdressBook():
    """List of address class"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    refrence_name = models.CharField(max_length=255, blank=False)
    address_line1 = models.CharField(max_length=255, blank=False)
    address_line2 = models.CharField(max_length=255, blank=True, null=True)
    adress_line3 = models.CharField(max_length=255, blank=True, null=True)
    pincode = models.IntegerField()
