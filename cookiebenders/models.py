import datetime

from django.db import models
from django.utils import timezone


class Sale(models.Model):

    num_cookies = models.IntegerField('Number of cookies', default=0)
    num_milk = models.IntegerField('Number of milk', default=0)

    cost = models.FloatField('Total cost of sale', default=0.0)

    # time_start = models.DateTimeField('Request date/time', default=timezone.now())
    # # delivery should be 15 minutes after request. Maybe default shouldnt be now? 
    # time_deliv = models.DateTimeField('Delivery request date/time', default=timezone.now() 
    #              + datetime.timedelta(minutes=15))
    time_start = models.DateTimeField('Request date/time')
    time_deliv = models.DateTimeField('Delivery request date/time')

    # payment can be 'C' for Cash or 'V' for Venmo
    PAYMENTS = (
    	('C', 'Cash'),
    	('V', 'Venmo'),
    )
    payment_meth = models.CharField('Payment method', max_length=1, choices=PAYMENTS)

    special_req = models.TextField('Special request', max_length=5000, blank=True)

    location = models.CharField('Delivery location', max_length=128)
    name = models.CharField('Name of customer', max_length=128)
    phone = models.CharField('Phone number of customer', max_length=16)

    # result can be 'S' for Success, 'N' for No-show, 'O' for other
    RESULTS = (
    	('S', 'Success'),
    	('N', 'No-show'),
    	('O', 'Other')
    )
    result = models.CharField('Result of sale', max_length=1, choices=RESULTS, blank=True)

    # Is the sale active (i.e. now is between sale start and deliv + 5 min buffer)?
    def is_active(self):
    	now = timezone.now()
    	return self.time_start <= now and now <= self.time_deliv + datetime.timedelta(minutes=5)

    def __unicode__(self):
        return str(self.id)

# Sale:
# num cookies (int)
# total cost (float, just to be safe)
# request start time (datetime obj)
# request delivery time (start + 15 min) 
# payment method (C or V, charfield)
# milk quantity? (int)

# special request (textfield, optional)
# result (choices: success S, no-show N)
# location (string)

# name?
# phone number?

# not a field, but the cookie saved to session should include the Sale id
# cookies can save name and number
