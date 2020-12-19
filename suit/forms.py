from django import forms
from .models import Contact, Product


class ContactForm(forms.ModelForm):
    # name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = Contact
        # fields = ['name', 'email', 'subject', 'message', 'advice']
        fields = '__all__'


class ProductForm(forms.ModelForm):

    class Meta:
        model   = Product
        fields  = '__all__'
        widgets = {
            "fabr_date": forms.SelectDateWidget()
        }
