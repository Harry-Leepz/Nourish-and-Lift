from django.shortcuts import render


def view_bag(request):
    """
    A view to return the shopping bag
    with items the customer wants to purchase
    """

    return render(request, 'bag/bag.html')
