from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm

from .models import Contact, Product
from .validators import MaxSizeFileValidator


class ContactForm(forms.ModelForm):
    # name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    class Meta:
        model  = Contact
        fields = '__all__'
        # fields = ['name', 'email', 'subject', 'message', 'advice']


class ProductForm(forms.ModelForm):
    name  = forms.CharField(min_length=3, max_length=50)
    image = forms.ImageField(required=False, validators=[MaxSizeFileValidator(max_file_size=2)])
    price = forms.IntegerField(min_value=1, max_value=1500000)

    def clean_name(self):
        name = self.cleaned_data["name"]
        exist = Product.objects.filter(name__iexact=name).exists()

        if exist:
            raise ValidationError("Este nombre ya existe")

        return name

    class Meta:
        model   = Product
        fields  = '__all__'
        widgets = {
            "fabr_date": forms.SelectDateWidget()
        }


class RegisterForm(UserCreationForm):
    class Meta:
        model  = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
