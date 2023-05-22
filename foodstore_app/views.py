from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import *

def home(request):
    all_products = Product.objects.all()
    context = {
        'products': all_products
    }
    return render(request, "foodstore_app/index.html", context)

def get_description_by_id(request, id):
    product = get_object_or_404(Product, id=id)
    context = {
        'product': product
    }
    return render(request, 'product_description.html', context)

def product_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'foodstore_app/product_list.html', context)

def all_customers(request):
    all_customers = Customer.objects.all()
    context = {
        'customers': all_customers
    }
    return render(request, 'all_customers.html', context)

def customer_detail(request, id):
    customer = get_object_or_404(Customer, id=id)
    context = {
        'customer': customer
    }
    return render(request, 'customer_detail.html', context)

def create_customer(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'create_customer.html')

def update_customer(request, id):
    customer = get_object_or_404(Customer, id=id)
    if request.method == 'POST':
        pass
    else:
        return render(request, 'update_customer.html', {'customer': customer})

def delete_customer(request, id):
    customer = get_object_or_404(Customer, id=id)
    if request.method == 'POST':
        pass
    else:
        return render(request, 'delete_customer.html', {'customer': customer})


def create_product(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'create_product.html')

def update_product(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        pass
    else:
        return render(request, 'update_product.html', {'product': product})

def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        pass
    else:
        return render(request, 'delete_product.html', {'product': product})


class registerView(CreateView):
    form_class = CustomUserForm
    success_url = reverse_lazy('newsapp:index')
    template_name = 'foodstore_app/register.html'