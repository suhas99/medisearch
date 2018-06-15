from django.contrib import admin

# Register your models here.
from medicine.models import Address, MedicalShop , Products ,Type


class MedicalShopAdmin(admin.ModelAdmin):
 list_display = ('name', 'phone', 'address')


class AddressAdmin(admin.ModelAdmin):
 list_display = ('line_1', 'line_2', 'city', 'state', 'lat', 'lng')

#class Medtype_idAdmin(admin.ModelAdmin)
#	list_display =('medtype_id')


class ProductsAdmin(admin.ModelAdmin):
 list_display = ('med_name', 'med_dosage', 'med_quantity', 'med_price' ,'medtype_id')#'Medtype_id')

class TypeidAdmin(admin.ModelAdmin):
 list_display = ('medtype_id', 'med_type')

 

	

				

admin.site.register(MedicalShop, MedicalShopAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Type, TypeidAdmin)
admin.site.register(Products, ProductsAdmin)
