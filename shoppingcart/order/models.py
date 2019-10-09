from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.conf import settings


class UserManager(BaseUserManager):
    """base user manager class"""
    use_in_migrations = True

    def _create_user(self, email, password, **extra):
        """create user"""
        if not email:
            raise ValueError('email not provided')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra)
        user.set_password(password)
        user.save(self._db)
        return user

    def create_user(self, email, password=None, **extra):
        """create normal user"""
        extra.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra)

    def create_superuser(self, email, password=None, **extra):
        """create normal user"""
        extra.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra)


class User(AbstractBaseUser, PermissionsMixin):
    """user model from abstract base class"""
    email = models.EmailField(max_length=255, blank=False, unique=True)
    name = models.CharField(max_length=256, blank=False, null=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superadmin = models.BooleanField(default=False)
    last_login = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    objects = UserManager()


class AddressBook(models.Model):
    """List of address class"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    refrence_name = models.CharField(max_length=255, blank=False)
    address_line1 = models.CharField(max_length=255, blank=False)
    address_line2 = models.CharField(max_length=255, blank=True, null=True)
    adress_line3 = models.CharField(max_length=255, blank=True, null=True)
    pincode = models.IntegerField(blank=False, null=False)


class Order(models.Model):
    """order model class"""
    token = models.CharField(max_length=255, blank=True)
    total = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Total Rupees')
    email_address = models.EmailField(max_length=255, blank=True)
    address = models.ForeignKey(AddressBook, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
