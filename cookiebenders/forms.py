from django import forms
from cookiebenders.models import Sale

# form for all sales
class SaleForm(forms.ModelForm):
    # number of cookies to be sold, minimum 3, max 24
    #num_cookies = forms.IntegerField(min_value=3, max_value=24)
    num_cookies = forms.IntegerField(label='num_cookies',
        widget=forms.NumberInput(attrs={
            'color':'black', 'width':'20px','min':'3','max':'24'})
    )

    # number of milk units to be sold, can be 0, max_value is 4 (arbitrary?)
    num_milk = forms.IntegerField(min_value = 0, max_value=4, label='num_milk')

    # Payment method as a radio button selection
    payment_meth = forms.ChoiceField(
        widget = forms.RadioSelect(attrs={'id':'payment_meth_radio', 
            'name':'payment_meth_radio', }),
        choices = (
            ('C', 'Cash'),
            ('V', 'Venmo'),    
        ),
        label='payment_method'
    )

    # Perhaps this should be a dropdown that updates?? give it autofill
    location = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder':'Delivery location (your room) as [hallname roomnumber]'}),
        max_length=128,
        label='delivery_location'
    )

    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder':'Your name'}),
        max_length=128,
        label='name'
        )

    phone = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder':'Your number to help find you'}),
        max_length=16,
        label='phone'
    )

    # Special request as a textbox, optional as specified in model (blank=True)
    special_req = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder':'Optional: Enter any special request with your order'}),
        max_length=5000,
        required=False,
        label='special_req'
    )

    class Meta:
        model = Sale
        fields = ('num_cookies', 'num_milk', 'location', 'name', 'phone', 'payment_meth', 
                    'special_req' )
        exclude = ('cost', 'time_start', 'time_deliv', 'result',)
