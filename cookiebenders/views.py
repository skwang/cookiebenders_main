from django.http import HttpResponse
from django.shortcuts import render
from cookiebenders.forms import SaleForm

# Create your views here.
def index(request):
	if request.method == 'POST':
		form = SaleForm(request.POST)
		if form.is_valid():
			return HttpResponse('Received form successfully')
		else:
			return HttpResponse('Form errors :( ')
	saleform = SaleForm()
	context_dict = {'saleform':saleform,}
	return render(request, 'cookiebenders/index.html', context_dict)