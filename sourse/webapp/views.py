from django.shortcuts import render

from webapp.models import Product


def main_page(request):
    product = Product.objects.order_by('updated_at')
    return render(request, 'main_page.html',{'product': product})