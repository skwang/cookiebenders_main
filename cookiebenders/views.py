from django.shortcuts import render
from cookiebenders.forms import SaleForm
# Create your views here.
def index(request):
	saleform = SaleForm()
	context_dict = {'saleform':saleform,}
	return render(request, 'cookiebenders/index.html', context_dict)