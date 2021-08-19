from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from django.contrib.auth.models import User

from products.models import Product
from .models import WishList, WishListItem


@login_required
def wishlist(request):
    """
    A view to render the user's wishlist
    """
    wishlist = None
    try:
        wishlist = WishList.objects.get(user=request.user)
    except WishList.DoesNotExist:
        pass

    context = {
        'wishlist': wishlist,
    }

    return render(request, 'wishlist/wishlist.html', context)


@login_required
def add_to_wishlist(request, product_id):
    """
    Add a product from the store to the
    wishlist for the logged in user
    """
    product = get_object_or_404(Product, pk=product_id)

    wishlist, created = WishList.objects.get_or_create(user=request.user)
    # Add product to the wishlist
    wishlist.products.add(product)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
