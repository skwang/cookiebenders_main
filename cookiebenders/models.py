import datetime

from django.db import models
from django.utils import timezone


class Sale(models.Model):

    num_cookies = models.IntegerField(default=0)
    num_milk = models.IntegerField(default=0)

    cost = models.FloatField(default=0.0)

    time_start = models.DateTimeField(default=timezone.now())
    # delivery should be 15 minutes after request
    time_deliv = models.DateTimeField(default=timezone.now() 
                 + datetime.timedelta(minutes=15))

    # payment can be 'C' for Cash or 'V' for Venmo
    payment_meth = models.CharField(max_length=1)
    special_req = models.TextField(max_length=5000)

    location = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    phone = models.CharField(max_length=16)

    # result can be 'S' for Success, 'N' for No-show, 'O' for other
    result = models.CharField(max_length=1)

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
