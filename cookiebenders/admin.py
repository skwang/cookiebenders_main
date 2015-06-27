from django.contrib import admin
from cookiebenders.models import Sale, Session, ServiceAvailable
# Register your models here.

#class Sale_Admin(admin.ModelAdmin):
#    fieldsets = [
#        (None,               {'fields': 
#            ['time_deliv', 'num_cookies', 'num_milk', 'special_req']}),
#        ('Payment Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#    ]
#class Sale_Admin(admin.ModelAdmin):


class Sale_Baker(Sale):
    class Meta:
        proxy = True

class Sale_Baker_Admin(admin.ModelAdmin):
    fields = ['num_cookies', 'num_milk', 'time_start', 'special_req', \
             'done_baking']

    def queryset(self, request):
        return self.model.objects.filter(done_baking=False)

class Sale_Deliverer(Sale):
    class Meta:
        proxy = True

class Sale_Deliverer_Admin(admin.ModelAdmin):
    fields = ['location', 'name', 'phone', 'payment_meth', 'cost', \
              'time_deliv', 'special_req', 'result']

    def queryset(self, request):
        return self.model.objects.filter(done_baking=True).filter(result='')

# Used to view all sales and correct mistakes
admin.site.register(Sale)
# Bakers use this to view unbaked sales
admin.site.register(Sale_Baker, Sale_Baker_Admin)
# Deliverers use this to view baked but undelivered sales
admin.site.register(Sale_Deliverer, Sale_Deliverer_Admin)
# View user sessions
admin.site.register(Session)
# View and change availability of cookiebending service
admin.site.register(ServiceAvailable)
