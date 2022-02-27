from django import forms
# from .models import Purchase, Product

class PurchaseForm(forms.ModelForm):
    # product = forms.ModelChoiceField(Product.objects.all(),
    #                                  label='Product',
    #                                  widget=forms.Select(attrs={'class': 'ui selection dropdown field-with'}))
    class Meta:
        pass
        # model = Purchase
        # fields = ['product', 'price', 'quantity']
