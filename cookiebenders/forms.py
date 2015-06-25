from django import forms
from cookiebenders.models import Sale

# form for all sales
class SaleForm(forms.ModelForm):
    # number of cookies to be sold, minimum 3, max 24
    num_cookies = forms.IntegerField(min_value=3, max_value=24)

    # number of milk units to be sold, can be 0, max_value is 4 (arbitrary?)
    num_milk = forms.IntegerField(min_value = 0, max_value=4)

    # Payment method as a radio button selection
    payment_meth = forms.ChoiceField(
        widget = forms.RadioSelect(attrs={'id':'payment_meth_radio', 
            'name':'payment_meth_radio', 'class':'form-control'}),
        choices = (
            ('C', 'Cash'),
            ('V', 'Venmo'),    
        )
    )

    # Special request as a textbox, optional as specified in model (blank=True)
    special_req = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control', 
            'placeholder':'Optional: Enter any special request with your order'}),
        max_length=5000,
    )

    # Perhaps this should be a dropdown that updates?? give it autofill
    location = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control', 
            'placeholder':'Delivery location (your room) as [hallname roomnumber]'}).
        max_length=128,
    )

    name = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control',
            'placeholder':'Your name'}),
        max_length=128,
        )

    phone = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control',
            'placeholder':'Your number to help find you'}),
        max_length=16,
    )

    class Meta:
        model = Sale
        fields = ('num_cookies', 'num_milk', 'payment_meth', 'special_req', 
                    'location', 'name', 'phone', )
        exclude = ('cost', 'time_start', 'time_deliv', 'result',)
