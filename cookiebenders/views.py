from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from cookiebenders.forms import SaleForm
from django.utils import timezone 
from cookiebenders.models import Sale
import datetime

# Create your views here.
def index(request):
	form_error = False

	# check if customer has an active order 
	has_active_order = False
	recent_order_id = request.session.get('recent_order')
	if recent_order_id:
		try:
			recent_order = Sale.objects.get(id=recent_order_id)
		except Sale.DoesNotExist: # case where we manually delete the Sale object, causes error
			request.session.flush() # ...only deletes in Django 1.8
			recent_order = None
		if recent_order and recent_order.is_active():
			has_active_order = True

	if request.method == 'POST' and not has_active_order:
		form = SaleForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			order_num_cookies = data['num_cookies']
			order_num_milk = data['num_milk']
			order_payment_meth = data['payment_meth']
			order_location = data['location']
			order_name = data['name']
			order_phone = data['phone']
			order_special_req = data['special_req']
			order_cost = find_cost(order_num_cookies, order_num_milk)
			order_time_start = timezone.now() + datetime.timedelta() # hack for form submit time...
			order_time_deliv = order_time_start + datetime.timedelta(minutes=15)

			new_order = Sale(num_cookies=order_num_cookies, num_milk=order_num_milk, 
							payment_meth=order_payment_meth, location=order_location,
							name=order_name, phone=order_phone, special_req=order_special_req,
							cost=order_cost, time_start = order_time_start, time_deliv = order_time_deliv,)
			new_order.save()

			request.session['recent_order'] = new_order.id 
			return HttpResponseRedirect("")

		else:
			form_error = True
			print form.errors

	if has_active_order:
		order_time_deliv = Sale.objects.get(id=recent_order_id).time_deliv
	else:
		order_time_deliv = None

	if not form_error:
		saleform = SaleForm()
	else:
		saleform = form

	context_dict = {'saleform':saleform, 'form_error': form_error, 'active_order': has_active_order, 
					'time_deliv':order_time_deliv}

	return render(request, 'cookiebenders/index.html', context_dict)

def find_cost(num_cookies, num_milk):
	# cost variables -- make global? 
	cost_of_12 = 9
	cost_of_6 = 5
	cost_of_3 = 3
	cost_of_1 = 1
	cost_of_milk = 1

	units_12 = num_cookies / 12
	units_6 = (num_cookies % 12) / 6
	units_3 = ((num_cookies % 12) % 6) / 3
	units_1 = (((num_cookies % 12) % 6) % 3)

	return cost_of_12 * units_12 + cost_of_6 * units_6 + \
			cost_of_3 * units_3 + cost_of_1 * units_1 + cost_of_milk * num_milk

