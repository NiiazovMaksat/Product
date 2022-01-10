from django.shortcuts import render, get_object_or_404

from webapp.forms import ProductForm
from webapp.models import Product


def main_page(request):
    product = Product.objects.order_by('category', 'name')
    return render(request, 'main_page.html', {'product': product})

def view_page(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, "view_page.html", context)

def edit_page(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'GET':
        form = Product(initial={
            'name': product.name,
            'description': product.description,
            'category': product.category,
            'count': product.count,
            'price': product.price
        })

        return render(request, 'edit.html', {'product': product, 'form': form})
    else:
        pass

def create_page(request):
    if request.method == "GET":
        form = ProductForm()
        return render(request, 'create.html', {'form': form})
