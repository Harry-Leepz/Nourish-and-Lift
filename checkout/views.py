from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    """
    A view to retrieve the bag from the session, render the checkout template
    and render the checkout form
    """

    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your bag is empty!")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout/html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)
