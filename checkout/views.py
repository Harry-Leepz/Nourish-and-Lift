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
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JMwr4CFuR9VVP0475wE4qoQuaBeAlNoR3OwZj0mdqq9j6lGHBDZjEwIn3fCF7jBmLMF7DSSxhJCXjowLJOuL9Ha00viMINqYZ',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
