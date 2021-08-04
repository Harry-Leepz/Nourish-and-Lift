from django.shortcuts import render, redirect, reverse


def view_bag(request):
    """
    A view to return the shopping bag
    with items the customer wants to purchase
    """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """
    A view to allow the users to add items to the bag
    with a quantity of their choosing
    """

    redirect_url = request.POST.get('redirect_url')
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """
    A view to allow the users the change the quantity of the product
    to a specified amount.
    """

    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
    else:
        bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))
