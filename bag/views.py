from django.shortcuts import (
    render, redirect, reverse,
    HttpResponse, get_object_or_404)
from django.contrib import messages
from products.models import Product


def view_bag(request):
    """
    A view to return the shopping bag
    with items the customer wants to purchase.
    """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """
    A view to allow the users to add items to the bag
    with a quantity of their choosing
    """

    product = get_object_or_404(Product, pk=item_id)
    redirect_url = request.POST.get('redirect_url')
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(request, f'Updated {product.name}')
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product.name}')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """
    A view to allow the users the change the quantity of the product
    to a specified amount.
    """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(request, f'Updated {product.name}')
    else:
        bag.pop(item_id)
        messages.success(request, f'Removed {product.name}')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """
    A view to allow the users to remove an item from the bag
    irrespective of the quantity.
    """

    try:
        product = get_object_or_404(Product, pk=item_id)
        bag = request.session.get('bag', {})

        bag.pop(item_id)
        messages.success(request, f'Removed {product.name}')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
