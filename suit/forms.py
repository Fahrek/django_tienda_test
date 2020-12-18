from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    # name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = Contact
        # fields = ['name', 'email', 'subject', 'message', 'advice']
        fields = '__all__'
