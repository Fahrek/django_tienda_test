from django.contrib import admin
from .models import Brand, Product, Contact
from .forms import ProductForm


class ProductAdmin(admin.ModelAdmin):
    list_display  = ['name', 'price', 'new', 'brand']
    list_editable = ['price']
    search_fields = ['name']
    list_filter   = ['brand', 'new']
    list_per_page = 100
    form = ProductForm


admin.site.register(Brand)
admin.site.register(Contact)
admin.site.register(Product, ProductAdmin)
