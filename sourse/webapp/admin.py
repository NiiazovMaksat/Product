from django.contrib import admin
from webapp.models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'count', 'price']
    list_filter = ['category']
    search_fields = ['name']
    fields = ['name', 'category', 'description', 'count', 'price']
    readonly_fields = []

admin.site.register(Product, ProductAdmin)