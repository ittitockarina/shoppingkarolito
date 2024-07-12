from .models import PaymentCard, ShippingInformation

from django import forms

class PaymentCardForm(forms.ModelForm):
    cvc = forms.CharField(
        label='',
        max_length=3,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'CVC',
        }),
    )
    date = forms.CharField(
        label='',
        max_length=5,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Date',
        }),
    )
    number = forms.CharField(
        label='',
        max_length=19,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Number',
        }),
    )

    class Meta:
        model = PaymentCard
        fields = ('cvc', 'date', 'number')  # Explicitly listing all required fields


class ShippingInformationForm(forms.ModelForm):
    address = forms.CharField(
        label='',
        max_length=255,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Address',
        }),
    )
    phone_number = forms.CharField(
        label='',
        max_length=40,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Phone Number',
        }),
    )

    class Meta:
        model = ShippingInformation
        fields = ('address', 'phone_number')
        exclude = ('customer',)
