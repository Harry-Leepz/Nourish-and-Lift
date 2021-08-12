from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from bag.contexts import bag_contents

import stripe


def checkout(request):
    """
    A view to retrieve the bag from the session, render the checkout template
    and render the checkout form
    """

    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your bag is empty!")
        return redirect(reverse('products'))

    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JMwr4CFuR9VVP0475wE4qoQuaBeAlNoR3OwZj0mdqq9j6lGHBDZjEwIn3fCF7jBmLMF7DSSxhJCXjowLJOuL9Ha00viMINqYZ',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
