from django.contrib import admin
from .models import Product,Order
from django.contrib.auth.models import Group
# Register your models here.

admin.site.site_header='Ankit Dashboard'

class ProductAdmin(admin.ModelAdmin):
    list_display=('name','category','quantity','cost_per_item','quantity_sold','sales')
    list_filter=['category']

class OrderAdmin(admin.ModelAdmin):
    list_display=('product','staff','order_quantity','date')
    
admin.site.register(Order,OrderAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.unregister(Group)