from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms  import UserCreationForm
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


class RegisterForm(UserCreationForm):

    class Meta:
       model = User
       fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']