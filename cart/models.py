from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save
from product.models import Product


# Create your models here.
class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(Product, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}''s cart - {}'.format(self.user.username, self.total)

    def to_dict(self):
        return {'user': self.user.username, 'total': self.total}


def calculate_cart_total(sender, instance, **kwargs):
    """
    Function that will get called just before the Cart object is saved. This method is connected with pre-save signal.
    It will recalculate the cart's total everytime a product is added or removed from the cart.
    :param sender:
    :param instance:
    :param kwargs:
    :return:
    """
    sub_total = 0

    # When the cart is created for the first time, it won't have a pk yet when this function is called. In that case
    # there won't be any products in the cart yet and we can ignore the logic inside
    if instance.pk is not None:
        for item in instance.items.all():
            sub_total += item.price
        instance.total = sub_total
    else:
        instance.total = 0


# Connect the function above to the signal
pre_save.connect(calculate_cart_total, Cart)
