from django.shortcuts import render, redirect


def view_bag(request):
    """
    A view to return the shopping bag
    with items the customer wants to purchase
    """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """
    A view to all the users to add items to the bag
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
    print(request.session['bag'])
    return redirect(redirect_url)
