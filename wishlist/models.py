from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class WishList(models.Model):
    """
    Model to show all product items within the users wishlist
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product,
                                      through="WishListItem",
                                      related_name='product_wishlists')

    def __str__(self):
        return f'WishList ({self.user})'


class WishListItem(models.Model):
    """
    A 'through' model, allowing users to add
    individual products to their wishlist.
    """

    product = models.ForeignKey(Product,
                                null=False,
                                blank=False,
                                on_delete=models.CASCADE)
    wishlist = models.ForeignKey(WishList,
                                 null=False,
                                 blank=False,
                                 on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name
