from django import forms

class CheckoutForm(forms.Form):
    PAYMENT_CHOICES = (
        ('cash_on_delivery', 'Cash on Delivery'),
        ('card', 'Card'),
    )
    first_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'name': 'first-name',
            'required': 'required'
        })
    )
    last_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'name': 'last-name',
            'required': 'required'
        })
    )
    company_name = forms.CharField(
        max_length=50,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'name': 'company-name'
        })
    )
    country = forms.ChoiceField(
        choices=[
            ('us', 'United States (US)'),
            ('uk', 'United Kingdom'),
            ('fr', 'France'),
            ('aus', 'Austria')
        ],
        widget=forms.Select(attrs={
            'class': 'form-control',
            'name': 'country'
        })
    )
    address1 = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'name': 'address1',
            'required': 'required',
            'placeholder': 'House number and street name'
        })
    )
    address2 = forms.CharField(
        max_length=255,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'name': 'address2',
            'placeholder': 'Apartment, suite, unit, etc. (optional)'
        })
    )
    city = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'name': 'city',
            'required': 'required'
        })
    )
    state = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'name': 'state',
            'required': 'required'
        })
    )
    zip_code = forms.CharField(
        max_length=10,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'name': 'zip',
            'required': 'required'
        })
    )
    phone = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'name': 'phone',
            'required': 'required'
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'name': 'email-address',
            'required': 'required'
        })
    )
    create_account = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'custom-checkbox',
            'id': 'create-account'
        })
    )
    different_address = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'custom-checkbox',
            'id': 'different-address'
        })
    )
    order_notes = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control pb-2 pt-2 mb-0',
            'cols': '30',
            'rows': '5',
            'placeholder': 'Notes about your order, e.g. special notes for delivery'
        })
    )
    terms_condition = forms.BooleanField(
        required=True,
        widget=forms.CheckboxInput(attrs={
            'class': 'custom-checkbox',
            'id': 'terms-condition'
        })
    )
    payment_method = forms.ChoiceField(choices=PAYMENT_CHOICES, widget=forms.RadioSelect)

