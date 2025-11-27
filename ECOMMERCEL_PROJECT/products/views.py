from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView
from .models import Product
from .forms import ProductForm

# Create your views here.


class ProductListView(ListView):
    model = Product
    template_name = "products/product_list.html"
    context_object_name = "products"

class ProductDetailView(DetailView):
    model = Product
    template_name = "products/product_detail.html"
    context_object_name = "product"

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = "products/product_form.html"
    success_url = ("products:product-list")
