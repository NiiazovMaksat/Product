from django.shortcuts import render, get_object_or_404, redirect

from webapp.forms import ProductForm
from webapp.models import Product, STATUS_CHOICES


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
        form = ProductForm(initial={
            'name': product.name,
            'description': product.description,
            'category': product.category,
            'count': product.count,
            'price': product.price
        })

        return render(request, 'edit.html', {'product': product, 'form': form, 'STATUS_CHOICES': STATUS_CHOICES})
    else:
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product.name = form.cleaned_data.get('name')
            product.description = form.cleaned_data.get('description')
            product.status = form.cleaned_data.get('status')
            product.count = form.cleaned_data.get('count')
            product.price = form.cleaned_data.get('price')
            product.save()
            return redirect("main")
        return render(request, 'edit.html', {'product': product, 'form': form, 'STATUS_CHOICES': STATUS_CHOICES})

def create_page(request):
    if request.method == "GET":
        form = ProductForm()
        return render(request, 'create.html', {'form': form})
    else:
        form = ProductForm(data=request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            description = form.cleaned_data.get('description')
            category = form.cleaned_data.get('category')
            count = form.cleaned_data.get('count')
            price = form.cleaned_data.get('price')
            new = Product.objects.create(name=name, description=description, category=category, count=count, price=price)
            return redirect("main")

        return render(request, 'create.html', {'form': form, 'STATUS_CHOICES': STATUS_CHOICES})
def delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', {'product': product})
    else:
        product.delete()
        return redirect("main")
