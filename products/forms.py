from django import forms
from .models import ProductReview


class ReviewForm(forms.ModelForm):

    class Meta:
        model = ProductReview
        exclude = ('product', 'user', 'date_added')
