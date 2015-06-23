from django.db import models
import datetime
# Create your models here.
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