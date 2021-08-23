from django import forms
from .widgets import CustomClearableFileInput
from .models import ProductReview, Product, Category


class ReviewForm(forms.ModelForm):

    class Meta:
        model = ProductReview
        exclude = ('product', 'user', 'date_added')


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super(). __init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
